from django.db import models
# Create your models here.


class ContractModel(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
