from django.urls import path
from django.contrib.auth import views as auth_views

# from store.views import HomePageView, ProductDetailView, CategoryView, CategoryDetailView, register
from store import views

app_name = 'store'


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_details'),
    path('categories/', views.CategoryView.as_view(), name='category'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_details'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
]
