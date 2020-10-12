from django.contrib import admin
from .models import Product, Cart


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity', 'unit_price']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id',]


