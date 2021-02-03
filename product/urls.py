from django.urls import path
from .views      import MainSlideProductsView, DrinkListView, ProductDetailView

urlpatterns = [
    path('/<int:product_id>', ProductDetailView.as_view(), name="detail"),
    path('', DrinkListView.as_view(), name='list'),
    path('/slider', MainSlideProductsView.as_view(), name='slider'),
]
