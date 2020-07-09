from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from .models import Category, Product, Contact, Pod_Category, Dostiopl, Comment
from cart.forms import CartAddProductForm
from .cart import Cart
from .forms import RatingForm, CommentForm
from django.http import HttpResponseRedirect, HttpResponse

# Страница с товарами
def product_list(request):
    categories = Category.objects.all()
    recomend_categories = Category.objects.filter(recomend=True)
    products = Product.objects.filter(available=True, recomend=True)
    recomend_tovar = Product.objects.filter(available=True, recomend=True)
    hit_prodaj = Product.objects.filter(available=True, hit_prodaj=True)
    hit_prodaj2 = Product.objects.filter(available=True, hit_prodaj2=True)
    new_tovar = Product.objects.filter(available=True, new_tovar=True)
    pod_category_one = Pod_Category.objects.all()
    carusel_tovar = Product.objects.filter(available=True, carusel_tovar=True)

    contact = Contact.objects.all()

    queryset_list = Product.objects.all()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Product.objects.all()

    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(name__icontains=query)

    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'product': queryset,
        'title': "List",
        'page_request_var': page_request_var,
        'categories': categories,
        'products': products,
        'recomend_tovar': recomend_tovar,
        'recomend_categories': recomend_categories,
        'hit_prodaj': hit_prodaj,
        'hit_prodaj2': hit_prodaj2,
        'new_tovar': new_tovar,
        'pod_category_one': pod_category_one,
        'carusel_tovar': carusel_tovar,
        'contact': contact,
    }
    return render(request, 'shop/product/list.html', context )

# Страница товара
def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    contact = Contact.objects.all()
    comments = product.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product_com = product
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'product': product,
        'categories': categories,
        'cart_product_form': cart_product_form,
        'contact': contact,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,

    }
    return render(request, 'shop/product/detail.html',  context)

'''все товары и поиск по ним'''
def prodall(request):
    katalog = Category.objects.all()
    categories = Category.objects.all()
    contact = Contact.objects.all()
    cart_product_form = CartAddProductForm()
    prodall = Product.objects.all()
    if request.user.is_staff or request.user.is_superuser:
        prodall = Product.objects.all()

    query = request.GET.get("q")
    if query:
        prodall = prodall.filter(name__icontains=query)

    paginator = Paginator(prodall, 3)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'prodall': queryset,
        'title': "List",
        'page_request_var': page_request_var,
        'katalog': katalog,
        'cart_product_form': cart_product_form,
        'contact': contact,
        'categories': categories,
    }
    return render(request, 'shop/product/prodall.html', context)

# Страница подкатегории
def pod_category_ditail(request, slug):
    katalog = Category.objects.all()
    cart_product_form = CartAddProductForm()
    pod_category = get_object_or_404(Pod_Category, slug=slug)
    contact = Contact.objects.all()
    categories = Category.objects.all()

    context = {
        'pod_category': pod_category,
        'cart_product_form': cart_product_form,
        'katalog': katalog,
        'contact': contact,
        'categories': categories,
    }
    return render(request, 'shop/product/pod_category_ditail.html', context)

# Страница категории
def catigory_ditail(request, slug):
    pod_category = Pod_Category.objects.all()
    category_one = get_object_or_404(Category, slug=slug)
    katalog = Category.objects.all()
    contact = Contact.objects.all()
    categories = Category.objects.all()

    context = {
        'category_one': category_one,
        'pod_category': pod_category,
        'katalog': katalog,
        'contact': contact,
        'categories': categories,
    }
    return render(request, 'shop/product/category_one.html', context)

# Страница контактов
def contact(request):
    contact = Contact.objects.all()
    katalog = Category.objects.all()
    categories = Category.objects.all()

    context = {
        'contact': contact,
        'katalog': katalog,
        'categories': categories,
        }
    return render(request,'shop/product/contact.html', context)

# Страница доставки и оплаты
def dostiopl(request):
    dostiopl = Dostiopl.objects.all()
    katalog = Category.objects.all()
    contact = Contact.objects.all()
    categories = Category.objects.all()

    queryset_list = Product.objects.all()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Product.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(name__icontains=query)

    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'product': queryset,
        'title': "List",
        'page_request_var': page_request_var,
        'dostiopl': dostiopl,
        'katalog': katalog,
        'contact': contact,
        'categories': categories,
        }
    return render(request,'shop/product/dostiopl.html', context)
