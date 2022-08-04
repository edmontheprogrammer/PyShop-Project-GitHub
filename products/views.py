from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Whenever the user sends a request to '/products'
# Django will call the 'index()' function which returns
# HttpResonse with "Home Page of the Product App"
# Uniform Resource Locator (Address)


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new_page_web_page1(request):
    return HttpResponse('New page 1!!!')


def new(request):
    return HttpResponse("new product page.")
