from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Contact, Pod_Category, Dostiopl, Carusel
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Страница с товарами
def product_list(request):
    categories = Category.objects.all()
    recomend_categories = Category.objects.filter(recomend=True)
    products = Product.objects.filter(available=True, recomend=True)
    recomend_tovar = Product.objects.filter(available=True, recomend=True)
    hit_prodaj = Product.objects.filter(available=True, hit_prodaj=True)
    new_tovar = Product.objects.filter(available=True, new_tovar=True)
    pod_category_one = Pod_Category.objects.all()
    carusel = Carusel.objects.all()
    carusel_tovar = Product.objects.filter(available=True, carusel_tovar=True)

    context = {
        'categories': categories,
        'products': products,
        'recomend_tovar': recomend_tovar,
        'recomend_categories': recomend_categories,
        'hit_prodaj': hit_prodaj,
        'new_tovar': new_tovar,
        'pod_category_one': pod_category_one,
        'carusel': carusel,
        'carusel_tovar': carusel_tovar,
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
    product = Product.objects.all()
    katalog = Category.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'pod_category': pod_category,
        'product': product,
        'cart_product_form': cart_product_form,
        'katalog': katalog,
    }
    return render(request, 'shop/product/pod_category_ditail.html', context)

# Страница категории
def catigory_ditail(request, slug):
    category_one = get_object_or_404(Category, slug=slug)
    pod_category = Pod_Category.objects.all()
    katalog = Category.objects.all()

    context = {
        'category_one': category_one,
        'pod_category': pod_category,
        'katalog': katalog,
    }
    return render(request, 'shop/product/category_one.html', context)

# Страница контактов
def contact(request):
    contact = Contact.objects.all()
    katalog = Category.objects.all()

    context = {
        'contact': contact,
        'katalog': katalog,
        }
    return render(request,'shop/product/contact.html', context)

# Страница доставки и оплаты
def dostiopl(request):
    dostiopl = Dostiopl.objects.all()
    katalog = Category.objects.all()

    context = {
        'dostiopl': dostiopl,
        'katalog': katalog,
        }
    return render(request,'shop/product/dostiopl.html', context)



