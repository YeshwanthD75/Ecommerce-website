import json
from .models import Order, Order_Product, Product

def get_total_quantity(request):
    cart_total = 0 

    if request.user.is_authenticated:
        customer = getattr(request.user, 'customer', None) 

        if customer:
            order, created = Order.objects.get_or_create(customer=customer, cart_complete=False)
            orderitems = Order_Product.objects.filter(order=order)
            cart_total = sum(item.quantity for item in orderitems)

    else:
        try:
            cart = json.loads(request.COOKIES.get('cart', '{}'))
            for product_id, data in cart.items():
                cart_total += data.get('quantity', 0)
        except json.JSONDecodeError:
            print("ERROR: Invalid JSON in cart cookie")

    return {'cart_total': cart_total}
