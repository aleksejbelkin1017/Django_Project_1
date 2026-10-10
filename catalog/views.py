from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.forms import ProductForm
from catalog.models import Product, Category
from catalog.services import get_products_by_category


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        # Автоматически назначаем владельцем текущего пользователя
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_update.html'
    success_url = reverse_lazy('catalog:products_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        # Пропускаем владельца или модератора (у него есть право delete_product)
        if product.owner != request.user and not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden("Вы не можете редактировать чужой продукт.")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        # Перенаправление на страницу просмотра товара
        return reverse('catalog:products_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:products_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        # Пропускаем владельца или модератора (у него есть право delete_product)
        if product.owner != request.user and not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden("Вы не можете удалить чужой продукт.")
        return super().dispatch(request, *args, **kwargs)


class ProductUnpublishView(LoginRequiredMixin, View):
    """Отмена публикации продукта. Доступно только модератору."""

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации.")

        product.is_published = False
        product.save()
        return redirect('catalog:products_detail', pk=product.pk)


class ProductListView(ListView):
    # Публичный список товаров — критерий «эндпоинт доступен анонимно»
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    # Карточка товара — только для авторизованных
    model = Product


class ContactsView(TemplateView):
    # Контакты — не про продукты, оставляем публичными
    template_name = "catalog/contacts.html"


class CategoryProductsView(ListView):
    """Список продуктов в указанной категории. Использует сервис с кешированием."""
    template_name = "catalog/category_products.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("pk")
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(Category, pk=self.kwargs.get("pk"))
        return context
