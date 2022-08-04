from django.urls import path
from . import views


# /products
# path() is a built-in function that accepts two paramters
# 'url' is what we want to users to type to
# on the browser to view the page and second
# parameter is the name of the functions inside
# the '.view' file
# pat('') with empty string repersents the product app's
#  index or the home of the '/products'
# path('') is the root of the app '/products'
# all the urls in this app starts with '/products'
urlpatterns = [
    # 'views.index' is p a reference to the index function
    # Note, not calling 'views.index' 'cause Django handles it
    path('', views.index),
    path('new_web_page1', views.new_web_page1),
    path('new', views.new),
]
