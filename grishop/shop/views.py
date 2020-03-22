from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

# Страница с товарами
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    recomend_categories = Category.objects.filter(recomend=True)
    products = Product.objects.filter(available=True, recomend=True)
    recomend_tovar = Product.objects.filter(available=True, recomend=True)
    hit_prodaj = Product.objects.filter(available=True, hit_prodaj=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'recomend_tovar': recomend_tovar,
        'recomend_categories': recomend_categories,
        'hit_prodaj': hit_prodaj
    })
# Страница товара
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form
                                                        }
                  )