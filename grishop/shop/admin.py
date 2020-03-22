from django.contrib import admin
from .models import Category, Product, Pod_Category
# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'recomend', 'id']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
# Модель подкаталога
class Pod_CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_podcategory', 'slug']
    prepopulated_fields = {'slug': ('name_podcategory', )}

admin.site.register(Pod_Category, Pod_CategoryAdmin)

# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', 'recomend', 'hit_prodaj']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Product, ProductAdmin)