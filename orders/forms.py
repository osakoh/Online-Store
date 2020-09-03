from django import forms
from .models import Order

"""
The order model is used to persist the items contained in the shopping cart when the user finally places an order.
Steps to be followed for creating a new order:
1) The user fills an order(Order model) form to get their details
2) A new 'Order' instance is created with the users data entered from step 1 and an associated 'OrderItem' instance
is created for each item in the cart.
3) Clear the shopping cart's contents and redirect the user to a success page
"""


class OrderCreateForm(forms.ModelForm):
    """
    used to create new 'Order' objects; this form is handled by a view in views.py
    """
    class Meta:
        model = Order  # selects the model to build the form
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']