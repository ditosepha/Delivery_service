from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    ROLES = (
        ("customer", "Customer"),
        ("courier", "Courier"),
        ("admin", "Admin")
    )

    role = models.CharField(max_length=20, choices=ROLES)

    USERNAME_FIELD = "username"

class Parcel(models.Model):
    STATUS = (
        ('pending',"Pending"),
        ('in transit',"In Transit"),
        ('delivered',"Delivered"),
    )

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=30, choices=STATUS)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="parcel")
    receiver_name = models.CharField(max_length=150)
    receiver_address = models.TextField()
    courier = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="courier_parcels", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField(null=True, blank=True)

class DeliveryProof(models.Model):
    parcel = models.OneToOneField(Parcel, on_delete=models.CASCADE)
    image = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)