from django.contrib import admin
from .models import Category, Product, Pod_Category, Gallery, Contact, Dostiopl, RaitingStar, Raiting
from django.utils.safestring import mark_safe
# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'recomend', 'id']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)



# Модель подкаталога
class Pod_CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_podcategory', 'slug', 'image_img']
    prepopulated_fields = {'slug': ('name_podcategory', )}

admin.site.register(Pod_Category, Pod_CategoryAdmin)

# Модель галлереи
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title_gallery', 'is_active']

admin.site.register(Gallery, GalleryAdmin)

# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', 'recomend',
                    'hit_prodaj', 'hit_prodaj2', 'new_tovar']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Product, ProductAdmin)



admin.site.register(Contact)
admin.site.register(Dostiopl)
admin.site.register(RaitingStar)
admin.site.register(Raiting)

"""изменение названия админка django в самом верху в админке"""
admin.site.site_title = "Администрирование магазина"
admin.site.site_header = "Администрирование магазина"