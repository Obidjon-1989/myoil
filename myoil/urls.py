from django.urls import path, include
from myoil.views import ProductViewSet,ServiceProviderProductViewSet,ReviewViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'products',ProductViewSet)
router.register(r'services',ServiceProviderProductViewSet)
router.register(r'reviews',ReviewViewSet)

urlpatterns = [
    path('', include(router.urls), name='products'),
]
