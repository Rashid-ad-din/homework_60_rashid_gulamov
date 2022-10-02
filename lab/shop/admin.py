from django.contrib import admin

from shop.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'category', 'rest', 'price', 'changed_at')
    list_filter = ('id', 'product', 'category', 'rest', 'price', 'changed_at')
    search_fields = ('product', 'category')
    fields = ('id', 'description', 'product', 'category', 'rest', 'price', 'created_at', 'changed_at')
    readonly_fields = ('id', 'created_at', 'changed_at')


admin.site.register(Product, ProductAdmin)
