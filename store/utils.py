import json
# Create your views here.
from .models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total': 0,
             'get_cart_total_items': 0,
             'shipping': False,
             }
    cartItems = order['get_cart_total_items']

    for i in cart:
        cartItems += cart[i]['quantity']

        try:
            product = StoreProduct.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_total_items'] += cart[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'productPicURL': product.productPicURL,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total,
            }
            items.append(item)

            if product.digital == False:
                order['shipping'] = True
        except:
            pass

    return {'items': items,
            'order': order,
            'cartItems': cartItems, }


def cartData(request):

    if request.user.is_authenticated:
        customer = request.user.storecustomer
        order, created = StoreOrder.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_total_items
    else:
        cookieData = cookieCart(request)
        items = cookieData['items']
        order = cookieData['order']
        cartItems = cookieData['cartItems']

    return {'items': items,
            'order': order,
            'cartItems': cartItems, }
