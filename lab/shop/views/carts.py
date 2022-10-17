from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView, DeleteView, TemplateView

from shop.forms.orders import OrderForm
from shop.models import Cart, Product


class AddProductToCart(RedirectView):
    def get(self, *args, **kwargs):
        cart_products = Cart.objects.all()
        pk = self.kwargs['pk']
        main_product = get_object_or_404(Product, pk=kwargs['pk'])
        Cart.add_to_cart(cart_products, main_product)
        return redirect('main')


class CartView(TemplateView):
    template_name = 'carts/cart_products.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        form = OrderForm()
        context['form'] = form

        cart = Cart.objects.all()
        context['cart'] = cart

        total = Cart.get_total(cart)
        context['total'] = total

        return self.render_to_response(context)


class CartProductDeleteView(DeleteView):
    template_name = 'carts/cart_product_delete.html'
    model = Cart
    context_object_name = 'product'
    success_url = reverse_lazy('cart')
