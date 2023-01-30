from django.urls import path, include

from books.views import BookAPI
from clients.views import RegisterAPI, LoginAPI, ClientsAPI
from boutique.views import BoutiqueAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('clients', ClientsAPI.as_view(), name='clients'),
    path('clients/<int:pk>', ClientsAPI.as_view(), name='clients'),
    path('books/', BookAPI.as_view(), name='books'),
    path('books/<int:pk>', BookAPI.as_view(), name='books'),
    path('boutiques/', BoutiqueAPI.as_view(), name='boutique'),
    path('boutiques/<int:pk>', BoutiqueAPI.as_view(), name='boutique'),
    path('cart/', include('cart.urls'), name='cart')
]
