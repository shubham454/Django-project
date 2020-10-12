from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_product, name='get-product'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('remove/', views.remove_from_cart, name='remove-cart'),
]