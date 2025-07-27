from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, index, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path("", index),
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
]
