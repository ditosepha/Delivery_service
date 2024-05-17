from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ParcelFilter
from rest_framework import filters
# Create your views here.

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class ParcelViewSet(ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [CanModifyParcel]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = ParcelFilter
        
class DeliveryProofViewSet(ModelViewSet):
    queryset = DeliveryProof.objects.all()
    serializer_class = DeliveryProofSerializer
    permission_classes = [DeliveryProofPermissions]

class CuorierParcelsViewSet(ModelViewSet):
    serializer_class = ParcelSerializer
    permission_classes = [IsCourier]

    def get_queryset(self):
        user = self.request.user
        return Parcel.objects.filter(courier=user)