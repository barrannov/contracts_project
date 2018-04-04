from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class ContractModel(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
