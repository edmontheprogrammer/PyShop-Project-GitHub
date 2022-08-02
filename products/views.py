from django.shortcuts import render
from django.http import HttpResponse

# /products -> index
# Uniform Resource Locator (Address)


def index(request):
    return HttpResponse('Hello World')


def new_page_web_page1(request):
    return HttpResponse('New page 1!!!')
