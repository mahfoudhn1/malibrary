# Generated by Django 4.1.2 on 2022-11-19 14:46

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=books.models.upload_to, verbose_name='Image'),
        ),
    ]
