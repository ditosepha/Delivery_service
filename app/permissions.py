import logging
from rest_framework.permissions import BasePermission, SAFE_METHODS

logger = logging.getLogger(__name__)

class CanModifyParcel(BasePermission):
    def has_permission(self, request, view):
        print(f"request method: {request.method}")
        print(f"user role: {request.user.role}")
        if request.user.is_authenticated:
            if request.user.role == 'courier' and request.method == "POST":
                return False
            else:
                return True
        
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.role == 'admin':
            return True
        elif request.user.role == 'courier':
            print(f"obj courier: {obj.courier}")
            print(f"user pk: {request.user.username}")
            if obj.courier_id == request.user.pk or obj.courier_id is None:
                return True
            else:
                return False
        elif request.user.role == 'customer':
            if request.method in ["PUT", "PATCH"]:
                if str(obj.sender) == str(request.user.username):
                    return True
                else: 
                    return False


class DeliveryProofPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role == "customer" and request.method == "POST":
                return False
            else:
                return True
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        if request.user.role == "admin":
            return True
        elif request.user.role == "courier":
            if request.method != "DELETE":
                return True
            else:
                return False
        elif request.user.role == "customer":
            if request.method in SAFE_METHODS:
                return True
            else: 
                return False