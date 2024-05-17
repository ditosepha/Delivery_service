from django.contrib import admin
from django.urls import path, include
from app.views import *
from rest_framework.routers import DefaultRouter
from .yasg import urlpatterns as swagger_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"users", CustomUserViewSet)
router.register(r"parcels", ParcelViewSet)
router.register(r"proofs", DeliveryProofViewSet)
router.register(r"courier", CuorierParcelsViewSet, basename="courier")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += swagger_urls