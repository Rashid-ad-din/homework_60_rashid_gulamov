from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView, DeleteView, TemplateView

from shop.models import Cart, Product


class AddProductToCart(RedirectView):
    def get(self, *args, **kwargs):
        cart_products = Cart.objects.all()
        pk = self.kwargs['pk']
        main_product = get_object_or_404(Product, pk=kwargs['pk'])
        if main_product in [cart_product.product for cart_product in cart_products]:
            cart_product = cart_products.get(product_id=pk)
            if main_product.rest > cart_product.amount:
                cart_product.amount += 1
                cart_product.save()
        else:
            cart = Cart()
            if main_product.rest > 0:
                cart.product = main_product
                cart.amount = 1
                cart.save()
        return redirect('main')


class CartView(TemplateView):
    template_name = 'carts/cart_products.html'
    model = Cart
    context_object_name = 'cart'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        cart = Cart.objects.all()
        context['cart'] = cart
        if cart:
            total = 0
            for product in cart:
                summ = product.product.price * product.amount
                total += summ
            context['total'] = total
        return self.render_to_response(context)


class CartProductDeleteView(DeleteView):
    template_name = 'carts/cart_product_delete.html'
    model = Cart
    context_object_name = 'product'
    success_url = reverse_lazy('main')
