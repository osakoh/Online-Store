from decimal import Decimal
from django.conf import settings
from shop.models import Product

"""
Each item in the cart contains the following:
• The ID of a Product instance as 
• The quantity selected for the product
• The unit price for the product
"""


class Cart(object):
    def __init__(self, request):
        """
        Cart constructor: Initialise the cart with a request object
        :param request:
        """
        self.session = request.session  # store the current session

        cart = self.session.get(settings.CART_SESSION_ID)  # Retrieve the cart from the  current session

        if not cart:  # if no cart is present in the current session
            # create an empty cart in the session by setting it to an empty dictionary
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

