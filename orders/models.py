from django.db import models
from shop.models import Product


class Order(models.Model):
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
        ordering = ('-created')

    def __str__(self):
        return "Order {}".format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.item.all())




