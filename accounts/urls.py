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
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.Login, name="login"),
    path('logout/', views.Logout, name="logout"),
    path('register/', views.Register, name="register"),
    path('', views.home, name="home"),
    path('user/', views.userPage, name="userPage"),

    path('customer/<str:pk>/', views.customer, name="customer"),
  
    path('UpdateOrder/<str:pk>/', views.UpdateOrder, name="UpdateOrder"),
    path('DeleteOrder/<str:pk>/', views.DeleteOrder, name="DeleteOrder"),
    
    path('delete_promo/<str:pk>/', views.delete_promo, name="delete_promo"),
    
    path('order/<int:order_id>/', views.order_details, name='order_details'),
    path('order/<int:order_id>/reorder/', views.reorder, name='reorder'),
    path('order/<int:order_id>/download-invoice/', views.download_invoice, name='download_invoice'),
    path('order/<int:order_id>/refund/', views.refund_request, name='refund_request'),

    path('account/', views.AccountSettings, name="AccountSettings"),
    
    path('category/', views.category, name="category"),
    path('delete_category/<int:pk>', views.delete_category, name="delete_category"),

    path('product_page/', views.product_page, name='product_page'),
    path('product_page/<int:pk>/', views.product_page, name='edit_product'),  # Editing an existing product
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
]

'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''
