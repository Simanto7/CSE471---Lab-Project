from django.db import models
from django.contrib.auth.models import User , Group
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='icon.png', null=True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    CATEGORYpopup = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )

    name = models.CharField(max_length = 200, null =True)
    price = models.FloatField(null =True)
    category = models.CharField(max_length = 200, null =True , choices = CATEGORYpopup)
    description = models.CharField(max_length = 200, null =True , blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null =True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    


class Order(models.Model):
    STATUSpopup = (
        ('0','Pending'),
        ('1','Out for delivery'),
        ('2','Delivered'),
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    products = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null =True)
    status = models.CharField(max_length = 200, null =True , choices = STATUSpopup)
    
    def __str__(self):
        return self.products.name

    

    
