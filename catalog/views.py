from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.forms import ProductForm
from catalog.models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_update.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        # Перенаправление на страницу просмотра статьи
        return reverse('catalog:products_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductListView(ListView):
    # Публичный список товаров — критерий «эндпоинт доступен анонимно»
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    # Карточка товара — только для авторизованных
    model = Product


class ContactsView(TemplateView):
    # Контакты — не про продукты, оставляем публичными
    template_name = "catalog/contacts.html"