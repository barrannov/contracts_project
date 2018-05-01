from django.db import models
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
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email





class ContractModel(models.Model):
    organisation_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    expire_date = models.DateField()
    author = models.ForeignKey(WebsiteUser, on_delete=models.SET_NULL, null=True)
    price_per_month = models.IntegerField()
    additional_notes = models.CharField(max_length=100)

    def __str__(self):
        return self.organisation_name
