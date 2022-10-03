from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from shop.forms import ProductForm, SearchForm
from shop.models import Product


def main_view(request: WSGIRequest):
    search_form = SearchForm
    products = Product.objects.exclude(rest=0).order_by('category', 'product')
    context = {
        'products': products,
        'search_form': search_form
    }
    return render(request, 'main.html', context)


def search_view(request: WSGIRequest):
    search_form = SearchForm
    search = request.GET.get('search')
    products = Product.objects.exclude(rest=0).filter(product__icontains=search).order_by('category', 'product')
    context = {
        'products': products,
        'search_form': search_form,
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


def product_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})


def edit_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    product_form = ProductForm(initial={
        'product': product.product,
        'description': product.description,
        'photo': product.photo,
        'category': product.category,
        'rest': product.rest,
        'price': product.price
    })
    if request.method == 'GET':
        return render(request, 'edit_product.html',
                      context={'product': product, 'product_form': product_form})
    form = ProductForm(request.POST)
    if not form.is_valid():
        return render(request, 'edit_product.html',
                      context={'product': product, 'product_form': product_form})
    product_form = ProductForm(request.POST)
    product = product_form.save()
    return redirect('product', pk=product.pk)


def delete_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'delete_product.html', context={'product': product})


def confirm_delete_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('main')
