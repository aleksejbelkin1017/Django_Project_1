from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]
