from django.contrib import admin
from django.urls import path

from webapp.views import (
    IndexView, 
    ProductView, 
    ProductCreateView, 
    ProductUpdateView, 
    ProductDeleteView, 
    ReviewCreateView, 
    ReviewUpdateView, 
    ReviewDeleteView,
)


app_name = 'webapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product_view'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/review/add/', ReviewCreateView.as_view(), name="review_create"),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name="review_update"),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name="review_delete"),
]   