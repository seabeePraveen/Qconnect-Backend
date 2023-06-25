from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, userid, password, **kwargs):
        try:
            user = CustomUser.objects.get(userid=userid)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
