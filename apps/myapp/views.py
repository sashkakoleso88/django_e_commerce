from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {
        "title": "Our products",
        "products": products,
    }
    return render(request, "myapp/list_of_products.html", context=context)


def contacts(request):
    return HttpResponse("<h1>You can call us: 000-555-222</h1>")
