from django.conf import settings
from django.db import models

from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SEND_TO_PROCEED = 'STP'
    PAID = 'PD'
    PROCEEDED = 'PRD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SEND_TO_PROCEED, 'отпралено в обработку'),
        (PROCEEDED, 'обрабатывается'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен'),
        (PAID, 'оплачен'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    created = models.DateTimeField(
        verbose_name='создан',
        auto_now_add=True,
    )

    update = models.DateTimeField(
        verbose_name='обновлен',
        auto_now_add=True,
    )

    status = models.CharField(
        verbose_name='статус',
        max_length=3,
        choices=ORDER_STATUS_CHOICES,
        default=FORMING,
    )

    is_active = models.BooleanField(
        verbose_name='активен',
        default=True,
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
            return f'текущий заказ {self.id}'

    def get_total_quantity(self):
            items = self.orderitems.select_related()
            return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity(self):
            items = self.orderitems.select_related()
            return len(items)

    def get_total_cost(self):
            items = self.orderitems.select_related()
            return sum(list(map(lambda x: x.quantity * x.product.price, items)))

    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quanaty += item.quantity
            item.product.save()


        self.is_active = False
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='orderitems',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        verbose_name='продукт',
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0
    )

    def get_product_cost(self):
        return self.product.price * self.quantity



