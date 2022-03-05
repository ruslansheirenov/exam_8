from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, ProductView, ProductCreateView, ProductUpdateView


app_name = 'webapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product_view'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]   