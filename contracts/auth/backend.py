from contracts.models import WebsiteUser
from django.contrib.auth.hashers import check_password

class AuthBackend:
    def authenticate(self, request, email=None, password=None):
        try:
            user = WebsiteUser.objects.get(email=email)
            if not check_password(password, user.password):
                return None
        except WebsiteUser.DoesNotExist:
            return None
        return user

    def get_user(self, user_id):
        try:
            return WebsiteUser.objects.get(pk=user_id)
        except WebsiteUser.DoesNotExist:
            return None
