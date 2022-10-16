from django.urls import path

from shop.views.carts import AddProductToCart, CartView, CartProductDeleteView
from shop.views.products import ProductsView, ProductView, ProductAddView, ProductEditView, ProductDeleteView, \
    ProductsByCategoryView

urlpatterns = [
    path('', ProductsView.as_view(), name='main'),
    path('add/', ProductAddView.as_view(), name='add_product'),
    path('products/<pk>/', ProductView.as_view(), name='product'),
    path('edit/<pk>/', ProductEditView.as_view(), name='edit_product'),
    path('delete/<pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('confirm-delete-product/<pk>/', ProductDeleteView.as_view(), name='confirm_delete_product'),
    path('category/<key>/', ProductsByCategoryView.as_view(), name='by_category'),
    path('cart/add/<pk>/', AddProductToCart.as_view(), name='add_to_cart'),
    path('cart/delete/<pk>/', CartProductDeleteView.as_view(), name='delete_cart_product'),
    path('confirm-delete-cart-product/<pk>/', CartProductDeleteView.as_view(), name='confirm_delete_cart_product'),
    path('cart/', CartView.as_view(), name='cart'),
]
