from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, ProductView


app_name = 'webapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product_view'),
]   