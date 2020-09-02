from .cart import Cart


def cart(request):
    """
    context processor: Used when you want a variable to be available globally to all templates. It is a Python function
    that takes a request object as an argument and returns a dictionary that gets added to the request context.
    :param request: is used to instantiate the cart and make it globally available for all templates
    :return: a variable 'cart' which is now globally available to templates
    """
    return {
        'cart': Cart(request)
    }