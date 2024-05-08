from django.contrib import admin
from django.urls import path, include
from app.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", CustomUserViewSet)
router.register(r"parcels", ParcelViewSet)
router.register(r"proofs", DeliveryProofViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
