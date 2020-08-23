from django.shortcuts import render
from .models import OrderItem, Item, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.models import Category, Contact

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return  render(request, 'orders/order/item_list.html', context)

def order_create(request):
    katalog = Category.objects.all()
    contact = Contact.objects.all()
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            katalog = Category.objects.all()
            return render(request, 'orders/order/created.html',
                          {'order': order,
                           'katalog': katalog,
                           'contact': contact,
                           })
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart,
                   'form': form,
                   'katalog': katalog,
                   'contact': contact,
                   })

