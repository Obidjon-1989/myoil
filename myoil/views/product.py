from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.db import models
from myoil.filters import ProductFilter
from django_filters import rest_framework as django_filters
from rest_framework import filters
from myoil.permissions import  IsAuthorOrReadonlyProduct

from myoil.models import Product, ServiceProviderProduct
from myoil.serializers import ProductSerializer, ServiceProviderProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadonlyProduct]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ProductFilter
    search_fields = ['brand', 'viscosity', 'oil_standards', 'description','oil_type', 'manufacturing_country']

    def list(self, request, *args, **kwargs):
        viscosity = request.query_params.get('viscosity', None)
        if viscosity:
            self.queryset = self.queryset.filter(viscosity=viscosity)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(brand=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Mahsulotga o'xshash mahsulotlarni olish
        related_products = Product.objects.filter(viscosity=instance.viscosity).exclude(id=instance.id)[:5]
        related_serializer = ProductSerializer(related_products, many=True)

        # Shu mahsulotga xizmat ko'rsatuvchi providerlar ro'yxatini olish

        service_providers = ServiceProviderProduct.objects.filter(oil_name=instance).order_by('price_per_liter').distinct()[:5]
        service_provider_serializer = ServiceProviderProductSerializer(service_providers, many=True)

        return Response({
            'product': serializer.data,
            'related_products': related_serializer.data,
            'service_providers': service_provider_serializer.data
        })

    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        top_products = Product.objects.annotate(avg_rating=models.Avg('reviews__rating')).order_by('-avg_rating')[:2]
        serializer = ProductSerializer(top_products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def average_rating(self, request, pk=None):
        product = self.get_object()
        reviews = product.reviews.all()

        if reviews.count() == 0:
            return Response({"average_rating": "Bu mahsulotga baho berilmagan!"})
        avg_rating = sum([review.rating for review in reviews]) / reviews.count()
        return Response({"average_rating": avg_rating})