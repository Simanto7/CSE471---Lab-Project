from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


from django.contrib.auth import authenticate, login, logout

from django.conf import settings

from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
import smtplib
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User


# from .decorators import unauthenticated_user

# Create your views here.
from .models import *
from store.models import *
from .forms import *
from .filters import OrderFilter

from .decorators import *
from .utils import *


@login_required(login_url='login')
@admin_only
def home(request):
    orders = StoreOrder.objects.filter(complete=True).order_by('-date_order')
    customers = StoreCustomer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    Delivered = orders.filter(status='2').count()
    Pending = orders.filter(status='0').count()
    out_of_delivery = orders.filter(status='1').count()
    
    # Calculate the total amount for all orders
    total_amount = sum(order.get_cart_total for order in orders)
    
    total_refund = orders.filter(refund_requested=True).filter(refund_status='1')
    
    total_refund_amount = sum(order.get_cart_total for order in total_refund)
    
    total_amount  = total_amount - total_refund_amount
    
    promos = PromoCode.objects.all().order_by('-id')
    
    form = PromoForm()
    
    if request.method == 'POST':
        form = PromoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
        

    context = {'orders': orders, 'customers': customers,
               'total_customers': total_customers,
               'total_orders': total_orders,
               'Delivered': Delivered,
               'Pending': Pending,
               'out_of_delivery': out_of_delivery,
                'total_amount': total_amount,
                'total_refund_amount': total_refund_amount,
                'form': form,
                'promos': promos
               }

    return render(request, 'accounts/dashboard_admin.html', context)


@login_required(login_url='login')
@admin_only
def category(request):
    categories = ProductCategory.objects.all().order_by('-id')
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('category'))
    context = {'categories': categories, 'form': form}
    return render(request, 'accounts/category.html', context)

@login_required
@admin_only
def delete_category(request, pk):
    category = ProductCategory.objects.get(id=pk)
    category.delete()
    return redirect(reverse('category'))


@login_required
@admin_only
def product_page(request, pk=None):
    
    if pk:
        # If a product ID (pk) is passed, it means we're editing an existing product
        product = get_object_or_404(StoreProduct, pk=pk)
        form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    else:
        # Otherwise, we are creating a new product
        product = None
        form = ProductForm(request.POST or None, request.FILES or None)
        
    # Handle form submission (whether it's adding or updating a product)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product_page')  # Redirect to the product page to show updated list

    # Get all products to display
    products = StoreProduct.objects.all().order_by('-id')

    context = {
        'form': form,
        'products': products,
        'product': product  # To distinguish between add and edit mode
    }

    return render(request, 'accounts/product_page.html', context)


@login_required
@admin_only
def delete_product(request, pk):
    product = get_object_or_404(StoreProduct, pk=pk)
    product.delete()
    return redirect('product_page')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_promo(request, pk):
    promo = PromoCode.objects.get(id=pk)
    promo.delete()
    return redirect(reverse('home'))


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):

    orders = request.user.storecustomer.storeorder_set.filter(complete=True).order_by('-date_order')
    customer = request.user.storecustomer.id
    customers = StoreCustomer.objects.filter(id=customer)

    total_orders = orders.count()
    Delivered = orders.filter(status='2').count()
    Pending = orders.filter(status='0').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders,
               'Delivered': Delivered,
               'Pending': Pending
               }

    return render(request, 'accounts/dashboard.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):

    customer = StoreCustomer.objects.get(id=pk)

    orders = customer.storeorder_set.filter(complete=True).order_by('-date_order')
    orders_count = orders.count()
    
    
    # Calculate the total amount for all orders
    total_amount = sum(order.get_cart_total for order in orders)
    
    total_refund = orders.filter(refund_requested=True).filter(refund_status='1')
    
    total_refund_amount = sum(order.get_cart_total for order in total_refund)
    
    total_amount  = total_amount - total_refund_amount

    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs

    context = {'customer': customer,
               'orders': orders,
               'orders_count': orders_count,
               'my_filter': my_filter,
                'total_amount': total_amount,
                'total_refund_amount': total_refund_amount,
               }

    return render(request, 'accounts/customer.html', context)



@login_required(login_url='login')
def order_details(request, order_id):
    order = get_object_or_404(StoreOrder, id=order_id)

   
    # Check if the user is authorized to view the order (e.g., the order belongs to the logged-in customer)
    if  not request.user.is_staff and order.customer != request.user.storecustomer:
        return redirect('unauthorized')  # Redirect if the customer does not own the order
    
    shipping_address = order.shippingaddress_set.first()
    context = {
        'order': order,
        'order_items': order.orderitem_set.all(),
        'shipping_address': shipping_address
        # Assuming OrderItem model is used for each product in the order
    }

    return render(request, 'accounts/order_details.html', context)

@login_required(login_url='login')
def refund_request(request, order_id):
    order = get_object_or_404(StoreOrder, id=order_id)

    if  not request.user.is_staff and order.customer != request.user.storecustomer:
        return redirect('unauthorized')
    
    order.refund_requested = True
    order.save()
    
    
    # Send email to the customer
    customer_subject = f"Refund Request for Order #{order.id}"
    customer_message = render_to_string(
        'accounts/refund_request_customer.html', 
        {'order': order, 'user': request.user}
    )
   
    msg = EmailMultiAlternatives(customer_subject, customer_message, settings.DEFAULT_FROM_EMAIL, [order.customer.email])
    msg.attach_alternative(customer_message, "text/html")
    msg.send()

    # Send email to the admin
    admin_subject = f"Refund Requested for Order #{order.id}"
    admin_message = render_to_string(
        'accounts/refund_request_admin.html', 
        {'order': order, 'user': request.user}
    )
    
    
    msg = EmailMultiAlternatives(  admin_subject, admin_message, settings.DEFAULT_FROM_EMAIL,
        [settings.ADMIN_EMAIL])
    msg.attach_alternative(admin_message, "text/html")
    msg.send()
    
    messages.warning(request, 'Refund requested successfully')
    
    return redirect('order_details', order_id=order_id)




@login_required(login_url='login')
def download_invoice(request, order_id):
    order = get_object_or_404(StoreOrder, id=order_id)

    if  not request.user.is_staff and order.customer != request.user.storecustomer:
        return redirect('unauthorized')
    
    shipping_address = order.shippingaddress_set.first()

    # Generate and download the invoice (example using `xhtml2pdf`)
    pdf = generate_invoice(order,shipping_address)  # Define this function in utils.py
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{order.id}.pdf"'
    return response

@login_required(login_url='login')
def reorder(request, order_id):
    original_order  = get_object_or_404(StoreOrder, id=order_id)

    
    if  not request.user.is_staff and original_order.customer != request.user.storecustomer:
        return redirect('unauthorized')

    # Remove any existing incomplete orders for the user
    existing_order = StoreOrder.objects.filter(
        customer=request.user.storecustomer, complete=False
    ).first()
    
    if existing_order:
        existing_order.delete()  # Delete the existing incomplete order
        
    new_order,created = StoreOrder.objects.get_or_create(
            customer=request.user.storecustomer, complete=False)
    
    
    # Recreate order items for the new order
    for item in original_order.orderitem_set.all():
        product = item.product
        quantity = item.quantity
        OrderItem.objects.create(
            product=product,
            order=new_order,
            quantity=quantity
        )

    return redirect('cart')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def UpdateOrder(request, pk):

    order = StoreOrder.objects.get(id=pk)

    form = OrderForm(instance=order)

    if request.method == 'POST':

        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))

    context = {'form': form
               }

    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def DeleteOrder(request, pk):

    order = StoreOrder.objects.get(id=pk)

    order.delete()

    return redirect(reverse('home'))


@unauthenticated_user
def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.groups.exists():
                login(request, user)
                messages.success(request, "Successfully Logged In "+username)
                return redirect('store')
            else:
                messages.error(
                    request, 'You are not authorized')
                return redirect('login')

        else:
            messages.error(request, "Invalid Credentials!")
    context = {
    }

    return render(request, 'accounts/login.html', context)


def Logout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('login')


@unauthenticated_user
def Register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = user.email
            username = form.cleaned_data.get('username')

            subject, from_email, to = 'Registration Successful', 'mishumishu5758@gmail.com', email
        
            text_content = (
                'Dear User,\n\n'
                'Thank you for registering with us. Your account has been successfully created.\n\n'
                'If you have any questions or need support, feel free to contact us.\n\n'
                'Best Regards,\n'
                'The Team'
            )
            html_content = (
                '<p>Dear User,</p>'
                '<p>Thank you for registering with us. Your account has been successfully created.</p>'
                '<p>If you have any questions or need support, feel free to <a href="mailto:mishumishu5758@gmail.com">contact us</a>.</p>'
                '<p>Best Regards,<br>The Team</p>'
            )

            # Create and send the email
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            StoreCustomer.objects.create(
                user=user, name=username, email=email
            )

            messages.success(request, 'Account was created for '+username)
            return redirect('login')
        else:
            messages.error(request, form.errors)

    context = {'form': form
               }

    return render(request, 'accounts/register.html', context)


@login_required(login_url='login')
def AccountSettings(request):

    # customer = request.user.customer.id
    # customers = Customer.objects.get(id=customer)
    user = request.user.storecustomer

    form = CustomerForm(instance=user)

    if request.method == 'POST':

        form = CustomerForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('AccountSettings')

    context = {'form': form
               }

    return render(request, 'accounts/account_settings.html', context)



