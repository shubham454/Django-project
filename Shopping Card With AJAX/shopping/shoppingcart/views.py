from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .cart import Cart
from .models import Product
from .forms import CartForm
import json


def get_product(request):
    products = Product.objects.all()
    form = CartForm()
    return render(request, 'products.html', {'products': products, 'cart': Cart(request), 'form': form})


def add_to_cart(request):
    form = CartForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        quantity = form.cleaned_data.get('quantity')
        product = Product.objects.get(name=name)
        cart = Cart(request)
        cart.add(product, product.unit_price, quantity)
        data = {
            'id': product.id,
            'name': name,
            'quantity': quantity,
            'total_price': (quantity*product.unit_price)
        }
        return JsonResponse(data)


def remove_from_cart(request):
    product_id = request.GET.get('id', None)
    product = Product.objects.get(id=product_id)
    data = {
        'deleted': True,
        'id': product_id
    }
    if product:
        cart = Cart(request)
        cart.remove(product)
        data['message'] = "Item deleted!"
    else:
        data['message'] = "Error!(object not selected)"
    return JsonResponse(data)
