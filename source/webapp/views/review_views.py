from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import ReviewForm
from webapp.models import Review, Product


#Создание отзыва

class ReviewCreateView(PermissionRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "review/create.html"

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('webapp:product_view', pk=product.pk)

#Редактирование отзыва

class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'reveiw/update.html'
    form_class = ReviewForm
    permission_required = "webapp.change_review"

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse("webapp:product_view", kwargs={"pk": self.object.product.pk})

#Удаление отзыва

class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    model = Review
    permission_required = "webapp.delete_review"

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:product_view", kwargs={"pk": self.object.product.pk})