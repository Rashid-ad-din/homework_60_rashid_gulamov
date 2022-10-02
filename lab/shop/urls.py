from django.urls import path

from shop.views.products import add_view, main_view

urlpatterns = [
    path('', main_view, name='main'),
    path('add/', add_view, name='add_product')
]
