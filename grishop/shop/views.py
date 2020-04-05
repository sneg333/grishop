from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Contact, Pod_Category
from cart.forms import CartAddProductForm


# Страница с товарами
def product_list(request):
    categories = Category.objects.all()
    recomend_categories = Category.objects.filter(recomend=True)
    products = Product.objects.filter(available=True, recomend=True)
    recomend_tovar = Product.objects.filter(available=True, recomend=True)
    hit_prodaj = Product.objects.filter(available=True, hit_prodaj=True)
    new_tovar = Product.objects.filter(available=True, new_tovar=True)
    pod_category_one = Pod_Category.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'recomend_tovar': recomend_tovar,
        'recomend_categories': recomend_categories,
        'hit_prodaj': hit_prodaj,
        'new_tovar': new_tovar,
        'pod_category_one': pod_category_one
    }
    return render(request, 'shop/product/list.html', context )

# Страница товара
def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'categories': categories,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html',  context)

# Страница подкатегории
def pod_category_ditail(request, slug):
    pod_category = get_object_or_404(Pod_Category, slug=slug)
    cart_product_form = CartAddProductForm()
    context = {
        'pod_category': pod_category,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/pod_category_ditail.html', context)

# Страница категории
def catigory_ditail(request, slug):
    category_one = Category.objects.get(slug=slug)
    pod_category = Pod_Category.objects.all()
    categories = Category.objects.all()

    context = {
        'category_one': category_one,
        'pod_category': pod_category,
        'categories': categories,
    }
    return render(request, 'shop/product/category_one.html', context)

# Страница контактов
def contact(request):
    contact = Contact.objects.all()

    context = {
        'contact':contact,
        }
    return render(request,'shop/product/contact.html', context)





