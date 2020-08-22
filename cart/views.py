from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from cart.cart import ShoppingCart
from cart.forms import AddProductForm


@require_POST
def cart_add(request, product_id):
    cart = ShoppingCart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = ShoppingCart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = ShoppingCart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

