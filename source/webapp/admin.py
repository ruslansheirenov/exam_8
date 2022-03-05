from django.contrib import admin

from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    fields = ['title', 'description', 'category', 'picture']

admin.site.register(Product, ProductAdmin)