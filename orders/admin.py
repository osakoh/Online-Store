from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """
    ModelInline(admin.TabularInline) is added so that it can be included as an inline in
    another admin(OrderAdmin) class.
    """
    model = OrderItem
    # this id_field must be a foreign key or a many-to-many field
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # sets fields to be displayed on the admin page
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code',
                    'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']  # filter section on the right side of admin page
    list_per_page = 15  # specify max amount of items to be displayed on the admin page
    inlines = [OrderItemInline]  # allows for the inclusion of another model on the same edit page as its related model
