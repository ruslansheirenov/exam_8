from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from webapp.models import Product

# Create your views here.

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