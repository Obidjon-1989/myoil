from django_filters import rest_framework as django_filters
from myoil.models import Product, Viscosity, OilStandard, ManufacturingCountry, ServiceProviderProduct, Region, District

class ProductFilter(django_filters.FilterSet):
    manufacturing_country = django_filters.ModelChoiceFilter(queryset=ManufacturingCountry.objects.all(), label="ManufacturingCountry")
    viscosity = django_filters.ModelChoiceFilter(queryset=Viscosity.objects.all(), label="Viscosity")
    oil_standards = django_filters.ModelMultipleChoiceFilter(queryset=OilStandard.objects.all(), label="OilStandard")
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains', label="Description")

    class Meta:
        model = Product
        fields = ['brand', 'viscosity', 'oil_standards', 'description','manufacturing_country','oil_type']

class ServiceProviderProductFilter(django_filters.FilterSet):
    region = django_filters.ModelMultipleChoiceFilter(queryset=Region.objects.all(), label="Region")
    district = django_filters.ModelMultipleChoiceFilter(queryset=District.objects.all(), label="District")
    min_price = django_filters.NumberFilter(field_name="price_per_liter", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price_per_liter", lookup_expr='lte')

    class Meta:
        model = ServiceProviderProduct
        fields = ['region','district','min_price', 'max_price', 'oil_name']

