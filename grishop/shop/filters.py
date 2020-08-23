from .models import Product, Brend
import django_filters

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Brend
        fields = ['title_brend']
