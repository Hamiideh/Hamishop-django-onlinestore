from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name=_('user'), related_name='orders')
    is_paid = models.BooleanField(_('Is_Paid'), default=False)

    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    phone_number = models.CharField(_('phone number'), max_length=15)
    address = models.CharField(_('address'), max_length=700)

    order_notes = models.CharField(_('order notes'), max_length=700, blank=True)

    zarinpal_authority = models.CharField(max_length=255, blank=True)
    zarinpal_ref_id = models.CharField(max_length=150, blank=True)
    zarinpal_data = models.TextField(blank=True)

    datetime_created = models.DateTimeField(_('created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('modified'), auto_now=True)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_price(self):
        # result = 0
        # for item in self.items.all():
        #     result += item.price * item.quantity
        # return result
        return sum(item.quantity * item.price for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    class Meta:
        unique_together = (('order', 'product'),)

    def __str__(self):
        return f'OrderItem {self.id}: {self.product} x {self.quantity} (price:{self.price})'
