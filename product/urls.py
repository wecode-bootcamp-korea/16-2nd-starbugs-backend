from django.urls import path

from product.views import DrinkListView

urlpatterns = [
    path('', DrinkListView.as_view())
]
