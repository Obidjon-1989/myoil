from rest_framework import serializers
from myoil.models import Product, Review, ServiceProviderProduct, CustomUser

class ProductSerializer(serializers.ModelSerializer):
    avg_rating=serializers.FloatField(read_only=True, required=False)
    brand = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ['id','brand','name','manufacturing_country','oil_type','viscosity','oil_standards','description','certificate','image','avg_rating']

class ServiceProviderProductSerializer(serializers.ModelSerializer):
    provider = serializers.PrimaryKeyRelatedField(read_only=True)
    provider_full_name = serializers.CharField(source='provider.full_name', read_only=True)
    provider_region = serializers.CharField(source='provider.region.name', read_only=True)
    provider_district = serializers.CharField(source='provider.district.name', read_only=True)
    provider_phone_number = serializers.CharField(source='provider.phone_number', read_only=True)
    provider_image = serializers.ImageField(source='provider.image', read_only=True)
    provider_location = serializers.CharField(source='provider.location', read_only=True)

    class Meta:
        model = ServiceProviderProduct
        fields = ['id','provider', 'oil_name', 'price_per_liter', 'service_price', 'description',
                  'provider_full_name', 'provider_region', 'provider_district',
                  'provider_phone_number', 'provider_image','provider_location']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    region = serializers.CharField(source='region.name', read_only=True)
    district = serializers.CharField(source='district.name', read_only=True)
    phone_number = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'company_name', 'region', 'district', 'phone_number', 'image','certificate_file','location']