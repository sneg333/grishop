from django.contrib import admin
from .models import Order, OrderItem, Item


class OrderItemInline(admin.TabularInline):

    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']


admin.site.register(Order)
admin.site.register(Item)
admin.site.register(OrderItem)