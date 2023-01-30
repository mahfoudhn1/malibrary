from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_POST
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer
from cart.cart import Cart


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    serializer = BookSerializer(data=product)
    if serializer.is_valid():
        cart.add(product=product, quantity=serializer.data['quantity'], update_quantity=serializer.data['update'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    cart.remove(product)
    return Response(cart)


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity'] = {'quantity': item['quantity']}
    # coupon_apply_form = CouponApplyForm()
    return Response({'cart': cart})
