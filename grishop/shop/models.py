from django.db import models
from django.core.urlresolvers import reverse

# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    recomend = models.BooleanField(default=False, verbose_name="Рекомендуемые")


    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

# Модель подкатегории
class Pod_Category(models.Model):
    category = models.ForeignKey(Category, related_name='products_pd', verbose_name="Категория")
    name_podcategory = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name_podcategory']
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name_podcategory

    def get_absolute_url(self):
        return reverse('shop:product_list_by_podcategory', args=[self.slug])

# Модель продукта
class Product(models.Model):
    STATUS_CHOICES_MENU = (
        ('smartf', 'Smartf'),
        ('naushn', 'Naushn'),
        ('noutbyk', 'Noutbyk'),
    )

    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория")
    pod_category = models.ForeignKey(Pod_Category, related_name='podcategory', verbose_name="Подкатегория")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    recomend = models.BooleanField(default=False, verbose_name="Рекомендуемые")
    glav = models.CharField(max_length=7, verbose_name='на главной', choices=STATUS_CHOICES_MENU, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']         # тут в примере круглые скобки
        index_together = [          # тут в примере круглые скобки
            ['id', 'slug']          # тут в примере круглые скобки
        ]                           # тут в примере круглые скобки
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
          return reverse('shop:product_detail', args=[self.id, self.slug])
