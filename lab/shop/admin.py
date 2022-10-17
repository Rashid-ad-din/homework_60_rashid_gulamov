from django.contrib import admin

from shop.models import OrderProductAmount
from shop.models.orders import Order
from shop.models.products import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'category', 'rest', 'price', 'changed_at')
    list_filter = ('id', 'product', 'category', 'rest', 'price', 'changed_at')
    search_fields = ('product', 'category')
    fields = ('id', 'product', 'description', 'photo', 'category', 'rest', 'price', 'created_at', 'changed_at')
    readonly_fields = ('id', 'created_at', 'changed_at')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_products', 'name', 'phone', 'address', 'created_at')
    list_filter = ('id', 'name', 'phone', 'address', 'created_at')
    search_fields = ('name', 'phone', 'address')
    fields = ('id', 'details', 'name', 'phone', 'address', 'created_at')
    readonly_fields = ('id', 'created_at', 'details')

    def details(self, obj):
        return ";\n".join([str(p) + 'Количество: ' + str(OrderProductAmount.objects.get(product_id=p.pk).order_amount)
                            for p in obj.products.all()])

    def get_products(self, obj):
        return ", ".join([p.product for p in obj.products.all()])


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
