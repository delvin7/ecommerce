from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import order, orderedItems
from products.models import product as Product  # Alias to avoid conflict
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def show_cart(request):
    if not request.user.is_authenticated:
        return redirect('account')

    try:
        customer = request.user.customer_profile
        cart = order.objects.get(owner=customer, order_status=order.cart_stage)
        items = cart.added_items.all()
    except ObjectDoesNotExist:
        cart = None
        items = []

    context = {
        'cart': cart,
        'items': items
    }
    return render(request, 'cart.html', context)

    
@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity', 1))
        product_id = request.POST.get('product_id')

        cart_obj, created = order.objects.get_or_create(
            owner=customer,
            order_status=order.cart_stage
        )

        product_obj = Product.objects.get(id=product_id)

        # Try to get the item first
        ordered_item, item_created = orderedItems.objects.get_or_create(
            owner=cart_obj,
            product=product_obj
        )

        if not item_created:
            # Already exists → increment quantity
            ordered_item.quantity += quantity
        else:
            # Newly created → set initial quantity
            ordered_item.quantity = quantity

        ordered_item.save()

    return redirect('cart')


def remove_from_cart(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(orderedItems, id=item_id)
        item.delete()
    return redirect('cart')

def checkout(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_profile
            total=float(request.POST.get('total'))
            order_obj=order.objects.get(owner=customer,order_status=order.cart_stage)
            if order_obj:
                order_obj.order_status=order.order_confirmed
                order_obj.total=total

                
                order_obj.save()
                status_messages= "Your order has been placed successfully!"
                messages.success(request, status_messages)
            else:
                status_messages="You do not have an active order"
                messages.error(request, status_messages)
        except Exception as e:
            status_messages="You do not have an active order"
            messages.error(request, status_messages)
    return redirect('orders')
@login_required(login_url='account')
def show_orders(request):
    user=request.user
    customer=user.customer_profile
    all_orders=order.objects.filter(owner=customer).exclude(order_status=order.cart_stage).order_by('-created_at')
    context={'orders':all_orders}
    return render(request,'orders.html',context)


        