from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from boutique.models import Boutique
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Review(models.Model):
    comments = models.CharField(max_length=500)
    rating = models.IntegerField(range(0, 5))


def upload_to(instant, filename):
    return f"books/media/{filename}".format(filename=filename)


class Book(models.Model):
    category = models.ForeignKey(Category, related_name='books',
                                 on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(_("Image"), upload_to=upload_to, blank=True, null=True)
    writer = models.CharField(max_length=200)
    price = models.FloatField()
    rate = models.IntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE,
                               blank=True, null=True)
    boutique = models.ForeignKey(Boutique, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('title',)
        # index_together = ('id',)

    def __str__(self):
        return self.title
