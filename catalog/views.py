from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    # Публичный список товаров — критерий «эндпоинт доступен анонимно»
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    # Карточка товара — только для авторизованных
    model = Product


class ContactsView(TemplateView):
    # Контакты — не про продукты, оставляем публичными
    template_name = "catalog/contacts.html"