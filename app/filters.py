from django_filters import rest_framework as filters 
from .models import Parcel

class ParcelFilter(filters.FilterSet):
    class Meta: 
        model = Parcel
        fields = ['title', 'status', 'sender']

