from django import forms
from .models import Product


class CartForm(forms.Form):
    INTEGER_CHOICES = [tuple([x.name, x.name]) for x in Product.objects.all()]
    name = forms.CharField(max_length=64, widget=forms.Select(choices=INTEGER_CHOICES))
    quantity = forms.IntegerField()