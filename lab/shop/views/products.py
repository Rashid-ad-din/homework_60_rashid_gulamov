from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from shop.forms import ProductForm
from shop.models import Product


def main_view(request: WSGIRequest):
    products = Product.objects.order_by('-changed_at')
    context = {
        'products': products
    }
    return render(request, 'main.html', context)


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        product_form = ProductForm
        return render(request, 'add_product.html', context={'product_form': product_form})
    product_form = ProductForm(request.POST)
    if not product_form.is_valid():
        return render(request, 'add_product.html', context={'product_form': product_form})
    product = product_form.save()
    return redirect('main')
