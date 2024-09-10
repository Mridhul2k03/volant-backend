from django.core.mail import send_mail
from django.conf import settings

def send_order_confirmation_email(order):
    subject = 'Order Confirmation'
    message = f'''
    Dear {order.user.username},

    Thank you for your order!

    Order Details:
    Product: {order.product.name}
    Quantity: {order.quantity}
    Total Price: {order.total_price}

    We will process your order soon.

    Best regards,
    mocs footwear
    '''
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [order.user.email]

    send_mail(subject, message, from_email, recipient_list)


def order_cancelled_mail(order):
    subject = 'Order Cancelled'
    message = f'''
    Dear {order.user.username},

    Your order has been cancelled.

    Best regards,
    mocs footwear
    '''
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [order.user.email]

    send_mail(subject, message, from_email, recipient_list)


