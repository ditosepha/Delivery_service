from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import CustomUser

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        User = get_user_model()
        try: 
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                if hasattr(user, "role") and user.role:
                    return user
                elif not hasattr(user, "role"):
                    return user
        except User.DoesNotExsit:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExsit:
            return None