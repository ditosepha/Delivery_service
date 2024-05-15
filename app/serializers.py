from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "password", "role", "id"]

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = "__all__"

    def validate(self, data):
        user_role = self.context['request'].user.role
        print("User Role:", user_role)
        if user_role == "admin":
            allowed_fields = ['title', 'description', 'status', 'receiver_name', 'receiver_address', "sender", 'courier', 'delivered_at']
        elif user_role == "courier":
            allowed_fields = ['courier', 'delivered_at', "status"]
        elif user_role == "customer":
            allowed_fields = []
        
        # Identify disallowed fields that are not allowed to be updated by the user role
        disallowed_fields = set(data.keys()) - set(allowed_fields)
        print("Disallowed Fields:", disallowed_fields)
        # Check if any disallowed fields have been modified
        if self.instance:
            for field in disallowed_fields:
                if field in data and getattr(self.instance, field) != data[field]:
                    raise serializers.ValidationError(f"User with role '{user_role}' is not allowed to update the '{field}' field.")
        
        return data

class DeliveryProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryProof
        fields = "__all__"