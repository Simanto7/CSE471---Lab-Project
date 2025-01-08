"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
   path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('updateItem/', views.updateItem, name="updateItem"),
	path('processOrder/', views.processOrder, name="processOrder"), 
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    
    # path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    path('wishlist/<int:user_id>/', views.wishlist_view, name='customer_wishlist'),
    
    
    path('product/<int:product_id>/review/', views.product_review, name='product_review'),
    
    path('apply_promo_code/', views.apply_promo_code, name='apply_promo_code'),
    
    path('compare/', views.compare, name='compare_products'),
    path('compare/<int:product_id>/', views.add_to_comparison, name='add_to_comparison'),
    path('compare/remove/<int:product_id>/', views.remove_from_comparison, name='remove_from_comparison'),
    
    
    path('sslcommerz_payment_success/', views.sslcommerz_payment_success, name='sslcommerz_payment_success'),
] 
