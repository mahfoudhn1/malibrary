from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from books.models import Book
from orders.models import Order


class TYPE_CHOICES(models.TextChoices):
    IND = 'individual',
    SHOP = "shop"


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    type_of_account = models.CharField(
        max_length=10,
        default=TYPE_CHOICES.IND,
        choices=TYPE_CHOICES.choices
    )

    def is_upperclass(self):
        return self.type_of_account in {self.IND, self.SHOP}

    def __str__(self):
        return self.user.username
