from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity' ,'price',]
    extra = 0
    min_num = 1


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'datetime_created', 'is_paid', 'num_of_items']
    ordering =['-datetime_created']

    inlines = [OrderItemInline,]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('items')


    def num_of_items(self, order):
        return order.items.count()


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
