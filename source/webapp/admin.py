from django.contrib import admin

from .models import Product, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    fields = ['title', 'description', 'category', 'picture']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['content']
    readonly_fields = ['created_at', 'updated_at']
    fields = ['content', 'product', 'rating', 'check_moder', 'created_at', 'updated_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)