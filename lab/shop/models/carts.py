from django.db import models


class Cart(models.Model):
    product = models.ForeignKey(
        to='shop.Product',
        verbose_name='Продукт',
        related_name='carts',
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(null=False, blank=False, verbose_name='Количество')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
