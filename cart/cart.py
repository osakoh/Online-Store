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

    def add(self, product, quantity=1, override_quantity=False):
        """
                                Key:values
        cart dictionary[product IDs]: {'quantity', 'price'}
        :param product: used to add/update the cart. Gets the ID for each product
        :param quantity: default quantity for a product in the cart =1
        :param override_quantity: Boolean to check if the default quantity is to be overridden with a new quantity(True)
        or whether the new quantity is to be added to the existing quantity(False). The default value is False
        :return:
        """
        product_id = str(product.id)  # converts the product ID(int) to string because Django uses JSON
        # to serialize session data, and JSON only allows string key names
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}  # price is cast to string, same reason as product_id
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity  # override the quantity with the given(new) quantity
        else:
            self.cart[product_id]['quantity'] += quantity  # add the new quantity to the existing quantity
        self.save()

