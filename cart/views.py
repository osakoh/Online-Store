from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


# @require_POST  # Decorator to require that a view only accepts the POST method.
def cart_add(request, product_id):
    """
    :param request:
    :param product_id: used to retrieve the Product instance and validate CartAddProductForm
    :return: the view redirects to the cart_detail
    """
    # creates a Cart object and assign it to cart
    cart = Cart(request)
    # selects a Product based on the product_id and returns 404 if the product doesn't exist
    product = get_object_or_404(Product, id=product_id)
    # creates an instance from the CartAddProductForm class and assign it to cart
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        """
        'cleaned_data' is only used if the basic form is used and not the ModelForm
        assigns the 'cleaned_data' to the variable 'cd'
        if the form is valid, a new product is added or the cart is updated
        """
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    """
    :param request:
    :param product_id: used to retrieve the Product instance and then, remove the product from the cart
    :return: redirects the user to the cart_detail URL
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)

    # the form is initialised with the current item quantity and the
    # override field is set to True so when the form is submitted to 'cart_add' view, the current quantity
    # is replace with a new one.
    for item in cart:
        item['update_quantity'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                              'override': True})

    context = {'cart': cart}
    return render(request, 'cart/detail.html', context)

