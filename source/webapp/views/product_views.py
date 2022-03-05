from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from webapp.models import Product
from webapp.forms import ProductForm, ProductDeleteForm

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
        reviews = self.object.reviews.filter(check_moder=True)
        context['reviews'] = reviews
        return context

#Создание товара

class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product/create.html"
    permission_required = "webapp.add_product"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

#Редактирование товара
    
class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm
    context_object_name = 'product'

    def has_permission(self):
        return super().has_permission()

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

#Удаление товара

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'product/delete.html'
    model = Product
    form_class = ProductDeleteForm
    success_url = reverse_lazy('webapp:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "POST":
            kwargs['instance'] = self.object
        return kwargs