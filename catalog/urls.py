from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("products/create/", views.ProductCreateView.as_view(), name="product_create"),
    path("products/update/<int:pk>/", views.ProductUpdateView.as_view(), name="product_update"),
    path("products/delete/<int:pk>/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]
