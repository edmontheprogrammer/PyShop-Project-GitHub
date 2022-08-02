from django.urls import path
from . import views


# /products

urlpatterns = [
    path('', views.index),
    path('new_page_web_page1', views.new_page_web_page1),
]
