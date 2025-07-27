from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, products_list, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path("", products_list, name="product_list"),
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
]
