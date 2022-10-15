from django.urls import path

from shop.views.products import ProductsView, \
    ProductView, ProductAddView, ProductEditView, ProductDeleteView, ProductsByCategoryView

urlpatterns = [
    path('', ProductsView.as_view(), name='main'),
    path('add/', ProductAddView.as_view(), name='add_product'),
    path('products/<pk>/', ProductView.as_view(), name='product'),
    path('edit/<pk>/', ProductEditView.as_view(), name='edit_product'),
    path('delete/<pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('confirm_delete/<pk>/', ProductDeleteView.as_view(), name='confirm_delete_product'),
    path('category/<key>/', ProductsByCategoryView.as_view(), name='by_category'),
]
