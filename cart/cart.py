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
        self.session = request.session  # assign the current session to self.session

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

    def save(self):
        self.session.modified = True  # current session is marked as 'modified' so it gets saved

    def remove(self, product):
        """
        :param product: selects the product to be removed from the cart
        :return:
        """
        product_id = str(product.id)  # same reason as casting product.id to str in add()

        if product_id in self.cart:  # checks if the product_id is in the cart and removes it
            del self.session['product_id']
            self.save()  # updates the modified cart

    def __iter__(self):
        """
        iterates over the items in the cart and get the products from the database
        """
        product_ids = self.cart.keys()  # gets the keys from the cart dictionary and assign it to product_ids
        products = Product.objects.filter(id__in=product_ids)  # use the product_ids to filter the Products from the DB

        cart = self.cart.copy()  # makes a copy of the cart dictionary

        for product in products:
            # from the cart dictionary, use the 'product.id' key to assess the 'product'
            # retrieve the product from the DB and add it to the cart dictionary
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])  # cast the price to a decimal type
            item['total_price'] = item['price'] * item['quantity']  # calculate the price of each item in the cart
            yield item  # returns a generator

    # tuple(i for i in (1, 2, 3))
    def __len__(self):
        """
        :return: count all items in the cart/the total number of items stored in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    # cart dictionary format- self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

    def get_total_price(self):
        """
        :return: the total cost of items in the cart
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        clears the cart session
        """
        del self.session[settings.CART_SESSION_ID]  # deletes the cart session
        self.save()  # updates the cart
