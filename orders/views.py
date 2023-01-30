from rest_framework.response import Response

from cart.cart import Cart
from orders.models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        data = request.data
        if data:
            order = data
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return Response({'order': order})


