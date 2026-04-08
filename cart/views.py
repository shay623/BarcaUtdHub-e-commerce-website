from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import Cart, CartItem, Order, OrderItem
from item.models import Item
from .forms import CheckoutForm

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id, is_sold=False)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        item=item,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'Increased {item.name} quantity to {cart_item.quantity}')
    else:
        messages.success(request, f'{item.name} added to cart!')
    
    return redirect(request.META.get('HTTP_REFERER', 'core:shop'))

@login_required
def remove_from_cart(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, item_id=item_id)
    
    item_name = cart_item.item.name
    cart_item.delete()
    messages.success(request, f'{item_name} removed from cart')
    
    return redirect('cart:cart_detail')

@login_required
def update_cart_item(request, item_id):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, item_id=item_id)
        
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated successfully')
        else:
            cart_item.delete()
            messages.success(request, 'Item removed from cart')
    
    return redirect('cart:cart_detail')

@login_required
def clear_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.items.all().delete()
    messages.success(request, 'Cart cleared successfully')
    return redirect('cart:cart_detail')



@login_required
def checkout(request):
    """Handle checkout process"""
    cart = get_object_or_404(Cart, user=request.user)
    
    # Check if cart is empty
    if not cart.items.exists():
        messages.warning(request, "Your cart is empty!")
        return redirect('cart:cart_detail')
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Create order
                    order = form.save(commit=False)
                    order.user = request.user
                    order.total_amount = cart.get_total_price()
                    order.save()
                    
                    # Create order items from cart
                    for cart_item in cart.items.all():
                        OrderItem.objects.create(
                            order=order,
                            item=cart_item.item,
                            quantity=cart_item.quantity,
                            price=cart_item.item.price  # Save price at time of purchase
                        )
                    
                    # Clear the cart
                    cart.items.all().delete()
                    
                    messages.success(request, f"Order #{order.id} placed successfully!")
                    return redirect('cart:order_confirmation', order_id=order.id)
                    
            except Exception as e:
                messages.error(request, f"Error processing order: {str(e)}")
                return redirect('cart:cart_detail')
    else:
        # Pre-fill form with user data if available
        initial_data = {
            'full_name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
        }
        form = CheckoutForm(initial=initial_data)
    
    context = {
        'form': form,
        'cart': cart,
    }
    return render(request, 'cart/checkout.html', context)


@login_required
def order_confirmation(request, order_id):
    """Display order confirmation page"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {
        'order': order,
    }
    return render(request, 'cart/order_confirmation.html', context)


@login_required
def order_history(request):
    """Display user's order history"""
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders,
    }
    return render(request, 'cart/order_history.html', context)


@login_required
def order_detail(request, order_id):
    """Display detailed view of a specific order"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {
        'order': order,
    }
    return render(request, 'cart/order_detail.html', context)