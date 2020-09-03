from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    :param order_id: function receives an order_id as a parameter
    sends an email notification when an order has been created successfully
    """
    order = Order.objects.get(id=order_id)
    subject = "Order number: {}".format(order.id)
    message = "Dear {}, \n" \
              "You have sucessfully placed an order for {}.\n" \
              "Your order ID is {}".format(order.first_name, order.items, order.id)
    mail_sent = send_mail(subject, message,
                          'customeradmin@mystore.com', [order.email])
    return mail_sent
