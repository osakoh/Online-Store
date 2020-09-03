from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib import messages


def order_create(request):
    """
    cart = Cart(request) gets the current cart session depending on the request method(POST/GET)
    if POST: a form is shown with the users details; if valid, a new order is created and saved(form.save()) in the DB.
             you then iterate over the cart items and create a new OrderItem for each cart item; the carts contents are
             cleared and the 'created.html' template is shown.
    if GET: an empty form is shown in the 'create.html' template.
    """
    cart = Cart(request)
    # if POST
    if request.method == 'POST':  # user clicks send
        form = OrderCreateForm(request.POST)  # step 1:shows a form Order instance containing the users details

        if form.is_valid():  # if all fields are filled with correct values and are not blank
            order = form.save()  # creates an order object and saves it to the DB

            # step 2: an associated 'OrderItem' instance is created for each item in the cart
            for item in cart:
                OrderItem.objects.create(
                    order=order, product=item['product'], price=item['price'], quantity=item['quantity']
                )
            # step 3: the shopping cart's contents are cleared and the user is redirected to a success page
            cart.clear()
            context = {'order': order}

            messages.success(request, 'Order created successfully')
            # return render(request, 'orders/order/created.html', context)
            return redirect('shop:product_list')
    # if GET
    else:
        form = OrderCreateForm()  # show the user an empty form if the send button isn't clicked
    context = {
        'cart': cart,
        'form': form
    }
    return render(request, 'orders/order/create.html', context)
