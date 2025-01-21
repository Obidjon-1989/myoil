from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from myoil.models import (
    Product,
    ServiceProviderProduct,
    OilType,
    Region,
    ManufacturingCountry,
    Review,
    District,
    OilStandard,
    Viscosity,
    CustomUser)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'company_name', 'region', 'district', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('region', 'district', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'company_name', 'phone_number')
    ordering = ('username',)

    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Information'), {  # Bo'lim nomi tarjima qilish uchun gettext_lazy ishlatilgan
            'fields': ('company_name', 'full_name', 'region', 'district', 'phone_number', 'image', 'certificate_file', 'location'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional Information'), {
            'fields': ('company_name', 'full_name', 'region', 'district', 'phone_number', 'image', 'certificate_file', 'location'),
        }),
    )

    def get_model_perms(self, request):
        """
        CustomUser modelini "Authentication and Authorization" bo'limiga qo'shish uchun
        umumiy menyu ruxsatlarini yoqish.
        """
        return {'add': True, 'change': True, 'delete': True, 'view': True}


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region')
    list_filter = ('region',)
    search_fields = ('name', 'region__name')
    ordering = ('name',)


admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)



admin.site.register(Product)
admin.site.register(ServiceProviderProduct)
admin.site.register(OilType)
admin.site.register(ManufacturingCountry)
admin.site.register(Review)
admin.site.register(OilStandard)
admin.site.register(Viscosity)


