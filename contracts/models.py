from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError('Email must be set!')
        user = self.model(email=email, full_name=full_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, full_name, password):
        user = self.create_user(email, full_name, password)
        user.is_admin = True
        user.save()
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

class WebsiteUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    full_name = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    objects = UserManager()


class ContractModel(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(WebsiteUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
