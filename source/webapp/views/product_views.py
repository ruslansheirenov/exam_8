from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from webapp.models import Product

# Create your views here.

#Список товаров

class IndexView(LoginRequiredMixin, ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'product/index.html'
    ordering = ['-id']
    paginate_by = 5
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

#Детальный просмотр отдного товара

class ProductView(DetailView):
    template_name = 'product/view.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.reviews.order_by("-created_at")
        context['reviews'] = reviews
        return context