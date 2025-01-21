from django.db import models
from .product import Product
from config import settings



class ServiceProviderProduct(models.Model):
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    oil_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_per_liter = models.DecimalField(max_digits=10, decimal_places=2)
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.provider} {self.oil_name}"

    class Meta:
        unique_together = ('provider', 'oil_name')