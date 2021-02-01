from django.urls import path
from order.views import ShoppingBasket

urlpatterns = [
    path('', ShoppingBasket.as_view())
]
