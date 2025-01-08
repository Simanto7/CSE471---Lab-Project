from django.contrib import admin
from .models import *
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','name','phone','email')
    search_fields = ['user','name','phone','email']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','digital')
    list_filter = ('digital', )
    search_fields = ['name',]

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','transaction_id','complete','date_order')
    list_filter = ('complete', )
    search_fields = ['customer','transaction_id',]

class ItemAdmin(admin.ModelAdmin):
    list_display = ('product','quantity','order',)
    search_fields = ['product','order',]

class AddressAdmin(admin.ModelAdmin):
    list_display = ('customer','order','address','city','state')
    list_filter = ('state', )
    search_fields = ['customer','address',]
    
    

# class ProductReviewAdmin(admin.ModelAdmin):
#     list_display = ('product', 'customer', 'rating', 'created_at', 'moderated')
#     list_filter = ('moderated',)
#     actions = ['approve_reviews', 'reject_reviews']

#     def approve_reviews(self, request, queryset):
#         queryset.update(moderated=True)

#     def reject_reviews(self, request, queryset):
#         queryset.update(moderated=False)

admin.site.register(StoreCustomer,CustomerAdmin)
admin.site.register(StoreProduct,ProductAdmin)
admin.site.register(StoreOrder,OrderAdmin)
admin.site.register(OrderItem,ItemAdmin)
admin.site.register(ShippingAddress,AddressAdmin)

admin.site.register(ProductCategory)
admin.site.register(WishlistItem)
admin.site.register(ProductReview)
admin.site.register(PromoCode)
admin.site.register(ProductComparison)