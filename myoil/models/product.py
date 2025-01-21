from django.db import models
from config import settings

class ManufacturingCountry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Viscosity(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

class OilStandard(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
class OilType(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
class Product(models.Model):
    brand = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    manufacturing_country= models.ForeignKey(ManufacturingCountry, on_delete=models.CASCADE)
    oil_type=models.ForeignKey(OilType, on_delete=models.CASCADE)
    viscosity = models.ForeignKey(Viscosity, on_delete=models.CASCADE)
    oil_standards = models.ManyToManyField(OilStandard)
    description=models.TextField(null=True, blank=True)
    certificate = models.FileField(upload_to='product/certificates/', blank=True, null=True)
    image = models.ImageField(upload_to='product/images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.brand})"

    class Meta:
        unique_together = ('name', 'brand', 'viscosity')