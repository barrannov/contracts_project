from .models import User


class AuthBackend:
    def authenticate(self, email=None, password=None):
        try:
            user = User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            return None
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
