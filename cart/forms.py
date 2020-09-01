from django import forms

'''
PRODUCT_QUANTITY_CHOICES = (
                    (1, "1"), 
                    (2, "2")........., 
                    (20, "20")
)
'''
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]  # a tuple containing the int, string representation


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    """
    quantity - selects a quantity between 1&20; it's renders as '<select><option ...>...</select>' in HTML
    coerce: cast the users input to integer

    override - indicates whether the quantity has to be added to any existing quantity in the cart
    for this product (False), or whether the existing quantity has to be overridden with the given
    quantity (True). You use a HiddenInput widget for this field, since you don't want to display it
    to the user. Renders as: <input type="hidden" ...> in HTML
    """


