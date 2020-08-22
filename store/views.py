from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView

from store.models import Product, Categories
from store.forms import RegisterForm
from cart.forms import AddProductForm


class HomePageView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'store_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_details.html'
    cart_form = AddProductForm()


class CategoryView(ListView):
    model = Categories
    template_name = 'store/category.html'
    context_object_name = 'category_list'


class CategoryDetailView(DetailView):
    model = Categories
    template_name = 'store/category_detail.html'
    context_object_name = 'category_details'


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('store_list:home')
    else:
        form = RegisterForm()
    return render(request, 'store/register.html', {'form': form})
