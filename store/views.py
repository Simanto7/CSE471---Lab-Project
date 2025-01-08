from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
import datetime
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.
from .models import *
from .utils import *
from django.db.models import Q, Avg

from .forms import *

from sslcommerz_lib import SSLCOMMERZ

def store(request):

    data = cartData(request)
    cartItems = data['cartItems']
    
    
    # Get filter parameters
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '')
    wishlist_action = request.GET.get('wishlist_action')
    product_id = request.GET.get('product_id')

    products = StoreProduct.objects.all().order_by('-date_created')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category_id:
        products = products.filter(category__id=category_id)
    
    
    for product in products:
        # Calculate the total rating sum and the number of reviews
        reviews = product.reviews.filter(moderated=True)
        if reviews.exists():
            total_rating = sum([review.rating for review in reviews])
            average_rating = total_rating / len(reviews)
        else:
            average_rating = 0  # No reviews, so average is 0

        # Add the average rating to each product
        product.average_rating = average_rating 
    
    categories = ProductCategory.objects.all()

    context = {
        'products': products,
        'cartItems': cartItems,
        'categories': categories,
        'form': ProductReviewForm(),
               }
    return render(request, 'store/store.html', context)


@login_required
def add_to_comparison(request, product_id):
    product = get_object_or_404(StoreProduct, id=product_id)
    comparison, created = ProductComparison.objects.get_or_create(user=request.user)
    if not comparison.has_product(product):
        comparison.add_product(product)
    return redirect('compare_products')



def compare(request):
    data = cartData(request)
    cartItems = data['cartItems']
    
    comparison, created = ProductComparison.objects.get_or_create(user=request.user)
    compared_products = comparison.get_products()

    # Calculate average ratings dynamically
    for product in compared_products:
        reviews = ProductReview.objects.filter(product=product, moderated=True)
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
        product.average_rating = avg_rating

    context = {
        'compared_products': compared_products,
        'cartItems': cartItems,
    }
    return render(request, 'store/compare.html', context)


@login_required
def remove_from_comparison(request, product_id):
    product = get_object_or_404(StoreProduct, id=product_id)
    comparison, created = ProductComparison.objects.get_or_create(user=request.user)
    
    if comparison.has_product(product):
        comparison.remove_product(product)
    
    return redirect('compare_products')


# View to handle the review form
def product_review(request, product_id):
    product = get_object_or_404(StoreProduct, id=product_id)

    # Handle Review Form Submission
    if request.method == 'POST':
        review_form = ProductReviewForm(request.POST)

        if review_form.is_valid():
            # Create a new review object
            review = review_form.save(commit=False)
            review.product = product
            review.customer = request.user.storecustomer  # Assuming user is authenticated
            review.moderated = False  # Set review as unmoderated initially
            review.save()

            # After saving the review, redirect to the product page or store page
            return redirect('store')  # Or you can redirect to a specific product page
    
    # # If it's a GET request, render the form in the modal
    # form = ProductReviewForm()
    # context = {
    #     'product': product,
    #     'form': form
    # }
    return redirect('store')

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(StoreProduct, id=product_id)
    if not WishlistItem.objects.filter(user=request.user, product=product).exists():
        WishlistItem.objects.create(user=request.user, product=product)
        messages.success(request, f"{product.name} has been added to your wishlist!")
    else:
        messages.warning(request, f"{product.name} is already in your wishlist!")
    return redirect('store')


# @login_required
def wishlist_view(request, user_id):
    
    
    data = cartData(request)
    cartItems = data['cartItems']
    
    
    # Get the customer by ID
    user = get_object_or_404(User, id=user_id)
    
    # Fetch the wishlist items for that user
    wishlist_items = WishlistItem.objects.filter(user=user)
    
    context = {
        'user': user,
        'wishlistItems': wishlist_items,
        'cartItems': cartItems,
    }
    return render(request, 'store/wishlist.html', context)


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(StoreProduct, id=product_id)
    WishlistItem.objects.filter(user=request.user, product=product).delete()
    messages.success(request, f"{product.name} removed from your wishlist!")
    return redirect('customer_wishlist',request.user.id)


def cart(request):

    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'store/cart.html', context)

@csrf_exempt
def checkout(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    
    

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'store/checkout.html', context)

def apply_promo_code(request):
    if request.method == "POST":
        promo_code = request.POST.get('promo_code').strip().lower()  # Remove spaces and make it case-insensitive
        data = cartData(request)
        order = data['order']

        try:
            promo = PromoCode.objects.get(code__iexact=promo_code, active=True)
            order.promo_code = promo
            order.save()
            messages.success(request, "Promo code applied successfully!")
        except PromoCode.DoesNotExist:
            messages.error(request, "Invalid promo code.")

    return redirect('checkout')


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.storecustomer
    product = StoreProduct.objects.get(id=productId)
    order, created = StoreOrder.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,
                                                         product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

@csrf_exempt
def processOrder(request):
    data = json.loads(request.body)

    transaction_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        customer = request.user.storecustomer
        order, created = StoreOrder.objects.get_or_create(
            customer=customer, complete=False)
        
            
    else:
        print('not logged in....')

        name = data['userFormData']['name']
        email = data['userFormData']['email']

        cookieData = cookieCart(request)
        items = cookieData['items']
        order = cookieData['order']

        customer, created = StoreCustomer.objects.get_or_create(
            email=email,)
        customer.name = name
        customer.save()

        order = StoreOrder.objects.create(
            customer=customer, complete=False)

        for item in items:
            product = StoreProduct.objects.get(id=item['product']['id'])

            orderItem = OrderItem.objects.create(
                product = product,
                order = order,
                quantity = item['quantity']
            )
        
    
    total = float(data['userFormData']['total']) 
    # total = float(data['userFormData']['total']) 

    if total == float(order.get_cart_total) :
        settings = { 'store_id': 'dubot66c79fa64e412', 'store_pass': 'dubot66c79fa64e412@ssl', 'issandbox': True }
        sslcz = SSLCOMMERZ(settings)
        post_body = {
            'value_a': order.id,
            'value_b': customer.email,
            'total_amount': total,
            'currency': "BDT",
            'tran_id': str(transaction_id),
            'success_url': request.build_absolute_uri(reverse('sslcommerz_payment_success')),
            'fail_url': request.build_absolute_uri(reverse('checkout')),
            'cancel_url': request.build_absolute_uri(reverse('checkout')),
            'emi_option': 0,
            'cus_name': customer.name,
            'cus_email': customer.email,
            'cus_phone': "01977242441",
            'cus_add1': data['shippingFormData']['address'],
            'cus_city': data['shippingFormData']['city'],
            'cus_country': "Bangladesh",
            'shipping_method': "NO",
            'multi_card_name': "",
            'num_of_item': 0,
            'product_name': "Test Product",
            'product_category': "General",
            'product_profile': "general",
        }
        response = sslcz.createSession(post_body) # API response
        return JsonResponse({'payment_url': response['GatewayPageURL']})
    else:
        print('did not match amount....')
        return JsonResponse({'error': 'Amount mismatch'}, status=400)  
    

@csrf_exempt
def sslcommerz_payment_success(request):
    data = request.POST
    transaction_id = data.get('tran_id')
    order_id = data.get('value_a')
    cus_email = data.get('value_b')
    customer = StoreCustomer.objects.get(email=cus_email)

    try:
        order = StoreOrder.objects.get(id=order_id)
        order.transaction_id = transaction_id
        order.complete = True
        order.save()

        if order.shipping:
            ShippingAddress.objects.create(
                customer=order.customer,
                order=order,
                address=data.get('address'),
                city=data.get('city'),
                state=data.get('state'),
                zipcode=data.get('zipcode'),
            )
        
            # Send email to the customer after the order is successfully placed
        order_details_url = request.build_absolute_uri(reverse('order_details', args=[order.id]))
        subject = f"Order #2025{order.id} Confirmation"
        message = f"Hello {customer.name},\n\nYour order #2025{order.id} has been successfully placed. The status of your order is: {order.get_status_display()}.\n\nYou can track the status of your order or view details on the following page: {order_details_url}\n\nThank you for shopping with us!"
        
        # Optionally, you can use an HTML template for the email body
        html_message = render_to_string('store/order_confirmation_email.html', {
            'order': order,
            'customer': customer,
            'order_details_url': order_details_url,
        })
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # Sender email
            [customer.email],  # Receiver email
            fail_silently=False,
            html_message=html_message  # Send HTML email
        )

        cart = {}
        response = JsonResponse('Payment successful.', safe=False)
        response.set_cookie('cart', json.dumps(cart), domain='', path='/')
        
        return redirect('store')

    except StoreOrder.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)

def terms_and_conditions(request):
    data = cartData(request)
    cartItems = data['cartItems']
    
    context = {
     
        'cartItems': cartItems,
    }
    
    return render(request, 'store/terms_and_conditions.html',context)