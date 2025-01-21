from myoil.serializers import ServiceProviderProductSerializer, ReviewSerializer
from myoil.models import Review, ServiceProviderProduct
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters import rest_framework as django_filters
from myoil.permissions import IsAuthorOrReadonlyServiceProvider
from myoil.filters import ServiceProviderProductFilter



class CustomPagination(PageNumberPagination):
    page_size = 5

class ServiceProviderProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadonlyServiceProvider]
    queryset = ServiceProviderProduct.objects.all()
    serializer_class = ServiceProviderProductSerializer

    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ServiceProviderProductFilter
    search_fields = ['oil_name', 'description']


    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Mahsulotga o'xshash mahsulotlarni olish
        another_pruducts = ServiceProviderProduct.objects.filter(user=instance.user).exclude(id=instance.id)[:5]
        another_pruducts_serializer = ServiceProviderProductSerializer(another_pruducts, many=True)

        return Response({
            'product': serializer.data,
            'Servisning boshqa mahsulotlari: ': another_pruducts_serializer.data,
        })



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer