from django.db import models
from shop.models import Product


class Order(models.Model):
    """
    this model stores customers information with a 'paid-BooleanField' which defaults to False.
    get_total_cost() is to calculate the total cost of items bought in a particular order.
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=8)
    city = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)  # initial date in db
    updated = models.DateTimeField(auto_now=True)  # changes whenever the update button is clicked
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "Order {}".format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())  # items here points to the 'related_name' in OrderItem


class OrderItem(models.Model):
    """
    this model stores the product, quantity, and price for each item.
    get_cost() returns the cost of items in an order.
    """
    # - an OrderItem belongs to one person(Order) and one person(Order)
    # can have multiple OrderItems (one-to-many relationship)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)  # an integer field but must be 1 or 0; can't be negative

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

