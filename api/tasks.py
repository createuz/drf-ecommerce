from celery import shared_task
from django.core.mail import send_mail, EmailMessage

from root.settings import EMAIL_HOST


@shared_task
def send_email(to_email, message, subject='Test subject', from_email='rajabovshohjahono3@gmail.com'):
    send_mail(
        subject,
        message,
        from_email,
        [to_email],
        fail_silently=True
    )
    email = EmailMessage('Test', 'Body', from_email, [to_email])
    email.send()
    return 'Done'