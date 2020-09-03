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
              "You have successfully placed an order.\n" \
              "Your order ID is {}".format(order.first_name, order.id)
    mail_sent = send_mail(subject, message,
                          'customeradmin@mystore.com', [order.email])
    return mail_sent

# pip install celery==4.2.0
# pip install eventlet
# celery -A mystore worker -l info -P gevent
