from django.db import models
from django.contrib.auth.models import User , Group
from PIL import Image


# Create your models here.
class StoreCustomer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='icon.png', null=True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)
    
    
# Product Category Model
class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.id)
    
class StoreProduct(models.Model):
    name = models.CharField(max_length = 200, null =True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True,blank=True)
    price = models.DecimalField(null =True,max_digits=7,decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank = True)
    description = models.CharField(max_length = 200, null =True , blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null =True)
    productPic = models.ImageField(default='placeholder.png', null=True, blank = True)
    
    @property
    def productPicURL(self):
        try:
            url = self.productPic.url
        except:
            url = ''

        return url
    
    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs)

        try:
            img = Image.open(self.productPic.url)

        # if img.height > 640 or img.width > 360:
            output_size = (640,360)
            img.thumbnail(output_size)
            img.save(self.productPic.url) 
        except:
            url = ''

         
    def __str__(self):
        return str(self.id)


class ProductComparison(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(StoreProduct)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
    def add_product(self, product):
        self.products.add(product)
    
    def remove_product(self, product):
        self.products.remove(product)
    
    def clear_products(self):
        self.products.clear()
    
    def get_products(self):
        return self.products.all()
    
    def get_products_count(self):
        return self.products.count()
    
    def has_product(self, product):
        return self.products.filter(pk=product.pk).exists()
    


# Review Model
class ProductReview(models.Model):
    product = models.ForeignKey(StoreProduct, related_name='reviews', on_delete=models.CASCADE)
    customer = models.ForeignKey(StoreCustomer, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)  # Rating from 1 to 5
    review_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    moderated = models.BooleanField(default=False)  # To mark the review as moderated/approved
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-created_at']  # Order by most recent review

    def save(self, *args, **kwargs):
        if self.rating < 1:
            self.rating = 1
        elif self.rating > 5:
            self.rating = 5
        super(ProductReview, self).save(*args, **kwargs)   



class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(StoreProduct, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'product')

class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_value = models.DecimalField(max_digits=5, decimal_places=2, help_text="Discount percentage")
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)
    
    
class StoreOrder(models.Model):
    STATUSpopup = (
        ('0','Pending'),
        ('1','Out for delivery'),
        ('2','Delivered'),
    )
    
    RefundStatus = (
        ('0','Pending'),
        ('1','Approved'),
        ('2','Declined'),
    )
    
    customer = models.ForeignKey(StoreCustomer,on_delete=models.CASCADE, blank=True, null=True)   
    date_order = models.DateTimeField(auto_now_add=True, null =True)
    complete = models.BooleanField(default=False,blank=True, null=True)
    transaction_id = models.CharField(max_length = 200, null =True)   
    status = models.CharField(max_length = 200, null =True ,default=0, blank=True, choices = STATUSpopup)
    refund_requested = models.BooleanField(default=False,blank=True, null=True)
    refund_status = models.CharField(max_length = 200, null =True ,default=0, blank=True, choices = RefundStatus)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        items = self.orderitem_set.all()

        for i in items:
            if i.product.digital == False:
                shipping = True


        return shipping

    @property
    def get_cart_total(self):
        items = self.orderitem_set.all()
        total = sum([item.get_total for item in items])
        
        # Apply promo code discount if available and active
        if self.promo_code and self.promo_code.active:
            discount = total * (self.promo_code.discount_value / 100)
            total -= discount
        return total
    
    @property
    def get_cart_total_before(self):
        items = self.orderitem_set.all()
        total = sum([item.get_total for item in items])
        return total
    

    @property
    def get_cart_total_items(self):
        items = self.orderitem_set.all()
        total = sum([item.quantity for item in items])
        return total

class OrderItem(models.Model):   
    product = models.ForeignKey(StoreProduct,on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(StoreOrder,on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null =True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    class Meta:
        unique_together = ('product', 'order')

    def __str__(self):
        return str(self.id)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(StoreCustomer,on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(StoreOrder,on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length = 200, null =True)
    city = models.CharField(max_length = 200, null =True)
    state = models.CharField(max_length = 200, null =True)
    zipcode = models.CharField(max_length = 200, null =True)

    def __str__(self):
        return str(self.id)