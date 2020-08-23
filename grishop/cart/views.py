from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, Category, Contact
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponseRedirect, HttpResponse

@require_POST
def cart_add(request, product_id):

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        form = form.cleaned_data
        cart.add(product=product,
                 quantity=form['quantity'],
                 update_quantity=form['update'])
    return redirect('cart:cart_detail')

# удаление товаров из корзины
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

# корзина
def cart_detail(request):
    katalog = Category.objects.all()
    categories = Category.objects.all()
    contact = Contact.objects.all()
    cart = Cart(request)

    return render(request, 'cart/detail.html', {'cart': cart,
                                                'katalog': katalog,
                                                'contact': contact,
                                                'categories': categories,
                                                })

