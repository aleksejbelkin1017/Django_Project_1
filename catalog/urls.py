from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, products_list, contacts, products_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", products_list, name="products_list"),
    path("products/<int:pk>/", products_detail, name="products_detail"),
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
]
