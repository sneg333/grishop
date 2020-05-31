from django.db import models
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Gallery(models.Model):
    title_gallery = models.CharField(max_length=400, verbose_name='название фото')
    photo_gallery = models.ImageField(upload_to='gallery', verbose_name='фото', blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Фотогаллерея'
        verbose_name_plural = 'Фотогаллерея'

    def __str__(self):
        return "%s, %s" % (self.title_gallery, self.is_active)

# Модель продукта
class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    tehnik_harakteristic = models.TextField(blank=True, verbose_name="Технические характеристики")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    recomend = models.BooleanField(default=False, verbose_name="Рекомендуемые")
    hit_prodaj = models.BooleanField(default=False, verbose_name="Хит продаж")
    new_tovar = models.BooleanField(default=False, verbose_name="Новый новар")
    carusel_tovar = models.BooleanField(default=False, verbose_name="карусель")
    product_gallery = models.ManyToManyField(Gallery, blank=True, verbose_name='фото товара')
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

# Модель подкатегории
class Pod_Category(models.Model):
    name_podcategory = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='podcategory/%Y/%m/%d/', blank=True, verbose_name="Изображение подкатегории")
    product = models.ManyToManyField(Product, verbose_name='товар')

    class Meta:
        ordering = ['name_podcategory']
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name_podcategory

    def get_absolute_url(self):
        return reverse('shop:pod_category_ditail', args=[self.slug])

    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    recomend = models.BooleanField(default=False, verbose_name="Рекомендуемые")
    pod_categoty = models.ManyToManyField(Pod_Category, verbose_name='подкатегории')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

# Модель контактов
class Contact(models.Model):
    title_contact = models.CharField(max_length=200, verbose_name='контакт')
    body_contact = RichTextUploadingField(blank=True, default='', verbose_name='текст')
    adress_one_contact = RichTextUploadingField(blank=True, default='', verbose_name='первый адрес')
    adress_toe_contact = RichTextUploadingField(blank=True, default='', verbose_name='второй адрес')
    tel = models.CharField(max_length=200, verbose_name='телефон')
    web = RichTextUploadingField(blank=True, default='', verbose_name='email')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакт'

    def __str__(self):
        return self.title_contact

# Модель оставка и оплата
class Dostiopl(models.Model):
    zagolovok = models.CharField(max_length=200, db_index=True, verbose_name='заголовок')
    predtekst = models.CharField(max_length=200, db_index=True,verbose_name='предтекст')
    text = RichTextUploadingField(blank=True, default='', verbose_name='первый адрес')

    class Meta:
        ordering = ['zagolovok']
        verbose_name = 'Доставка и оплата'
        verbose_name_plural = 'Доставка и оплата'

    def __str__(self):
        return self.zagolovok
