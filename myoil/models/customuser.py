from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from myoil.models import Region, District


phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Phone number must be in the format: '+998xxxxxxxxx'."
)

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150, null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True, null=True)
    image = models.ImageField(upload_to='product/service_providers/', null=True, blank=True)
    certificate_file = models.FileField(upload_to='product/brandcertificates/', null=True, blank=True)
    location = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.username
