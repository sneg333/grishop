from django.db import models
from shop.models import Product
from django.conf import settings

class Item(models.Model):
    title_item = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title_item

    class Meta:
        verbose_name = 'элемент'
        verbose_name_plural = 'элементы'


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name = 'детали заказа'
        verbose_name_plural = 'детали заказов'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, verbose_name="имя")
    last_name = models.CharField(max_length=50, verbose_name="фамилия")
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name="адрес")
    postal_code = models.CharField(max_length=20, verbose_name="телефон")
    city = models.CharField(max_length=500, verbose_name="комментарий")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, verbose_name="Выполнено")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())



