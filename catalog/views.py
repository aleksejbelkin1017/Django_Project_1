from django.shortcuts import render
from catalog.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")
