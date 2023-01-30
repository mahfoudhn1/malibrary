from django.contrib.auth.models import User
from django.db import models
# from books.models import Book


# Create your models here.

class Boutique(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    rate = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=12)
    # books = models.ManyToManyField(Book, null=True, blank=True)
    picture = models.CharField(max_length=2000)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, blank= True, null=True)

    def __str__(self):
        return self.name
