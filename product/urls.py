from django.urls import path

from .views      import ProductDetailView, DrinkListView

urlpatterns = [
    path('', DrinkListView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view(), name="detail"),
]
