from django.urls import path
from .views      import MainSlideProductsView, DrinkListView

urlpatterns = [
    path('', DrinkListView.as_view(), name='list'),
    path('/slider', MainSlideProductsView.as_view(), name='slider')
]
