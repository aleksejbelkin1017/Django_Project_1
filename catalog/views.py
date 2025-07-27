from django.shortcuts import render


def index(request):
    return render(request, "base.html")


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")
