from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(user_email):
    subject = "Welcome to Our App 🎉"
    message = "Thank you for registering. We're excited to have you!"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
    return f"Email sent to {user_email}"
