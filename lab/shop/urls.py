from django.urls import path

from shop.views.products import add_view, main_view, product_view, search_view, edit_view, delete_view, \
    confirm_delete_view

urlpatterns = [
    path('', main_view, name='main'),
    path('add/', add_view, name='add_product'),
    path('/search/', search_view, name='search'),
    path('/products/<pk>/', product_view, name='product'),
    path('edit/<pk>/', edit_view, name='edit_product'),
    path('delete/<pk>/', delete_view, name='delete_product'),
    path('confirm_delete/<pk>/', confirm_delete_view, name='confirm_delete_product'),
]
