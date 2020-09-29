from django.contrib import admin
from .models import User, Role, Product, Order, OrderItem


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email',
                    'password', 'is_active', 'role']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'vendor',
                    'order_status']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price', 'order']


admin.site.register(Role, RoleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
