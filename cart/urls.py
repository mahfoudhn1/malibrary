from django.urls import path
from .views import *

urlpatterns = [
    path('add/', cart_add, name='cart_add'),
    path('remove/', cart_remove, name='cart_remove'),
    path('detail/', cart_detail, name='cart_detail'),
]
