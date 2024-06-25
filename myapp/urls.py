from django.urls import path
from .views import (
    CreateProductView,
    GetProductListView,
    deleteAllProductView
)

urlpatterns = [
    path("products", GetProductListView.as_view(), name="get-all-products"),
    path("product/create", CreateProductView.as_view(), name="create-product"),
    path("product/delete-all", deleteAllProductView.as_view(), name="delete-all-products"),
]
