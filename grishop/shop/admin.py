from django.contrib import admin
from .models import Category, Product, Pod_Category, Gallery, Contact, Dostiopl
# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'recomend', 'id']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
# Модель подкаталога
class Pod_CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_podcategory', 'slug',]
    prepopulated_fields = {'slug': ('name_podcategory', )}

admin.site.register(Pod_Category, Pod_CategoryAdmin)

# Модель галлереи
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title_gallery', 'is_active']

admin.site.register(Gallery, GalleryAdmin)

# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', 'recomend', 'hit_prodaj', 'new_tovar']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Product, ProductAdmin)

# Модель комментариев
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['title_com', 'comment_email']

admin.site.register(Contact)
admin.site.register(Dostiopl)