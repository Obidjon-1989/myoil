from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadonlyServiceProvider(BasePermission):
    def has_permission(self, request, view):
        # GET so'rovlar uchun ruxsat
        if request.method in SAFE_METHODS:
            return True

        # POST va boshqa yozuv so'rovlari uchun ruxsat faqat autentifikatsiya qilingan userga
        return request.user.is_authenticated and request.user.groups.filter(name="ServiceProvider").exists()

    def has_object_permission(self, request, view, obj):
        # GET va boshqa xavfsiz so'rovlar uchun ruxsat
        if request.method in SAFE_METHODS:
            return True

        # Obyektga ega so'rovlar uchun faqat owner bo'lsa

        return obj.provider == request.user and request.user.groups.filter(name="ServiceProvider").exists()


class IsAuthorOrReadonlyProduct(BasePermission):
    def has_permission(self, request, view):
        # GET so'rovlar uchun ruxsat
        if request.method in SAFE_METHODS:
            return True

        # POST va boshqa yozuv so'rovlari uchun ruxsat faqat autentifikatsiya qilingan userga
        return request.user.is_authenticated and request.user.groups.filter(name="Manfacturer").exists()

    def has_object_permission(self, request, view, obj):
        # GET va boshqa xavfsiz so'rovlar uchun ruxsat
        if request.method in SAFE_METHODS:
            return True

        # Obyektga ega so'rovlar uchun faqat owner bo'lsa

        return obj.brand == request.user and request.user.groups.filter(name="Manfacturer").exists()

