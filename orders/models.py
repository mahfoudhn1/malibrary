from django.contrib.auth.models import User
from django.db import models
from books.models import Book


class shipping(models.TextChoices):
    domicile = 'domicile'
    desk = 'desk'


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    shipping = models.CharField(
        max_length=10,
        default=shipping.desk,
        choices=shipping.choices
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    # order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, blank=True, null= True)
    # product = models.ForeignKey(Book, related_name='order_items', on_delete=models.CASCADE, blank = True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
