from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Position(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price = models.IntegerField()


class Order(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
    position_id = models.JSONField(default=list)
    price = models.IntegerField()
