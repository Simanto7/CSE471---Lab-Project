from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *
from store.models import *

class CustomerForm(ModelForm):
    class Meta:
        model = StoreCustomer
        fields = '__all__'
        exclude = ['user']
    
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['name'].widget.attrs['readonly'] = True

class OrderForm(ModelForm):
    class Meta:
        model = StoreOrder
        fields = '__all__'

class PromoForm(ModelForm):
    class Meta:
        model = PromoCode
        fields = ['code','discount_value']

class CategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name']

class ProductForm(ModelForm):
    class Meta:
        model = StoreProduct
        fields = ['name','category','price','description','productPic']
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
                