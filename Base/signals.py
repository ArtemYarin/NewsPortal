from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Post, Subscribers


@receiver(post_save, sender=Post)
def notify_managers_news(sender, instance, created, **kwargs):
    if created:
        subject=instance.title
    else:
        subject=f'News {instance.title} has been changed'

    """
    post_category = instance.category
    recipient = []
    recipients = {}
    for i in post_category:
        recipient = i.Subscribers_set.all().user
        for j in recipient:
            recipients[j] = j.email
    """
            
    send_mail(
        subject=subject,
        message=instance.text[:50],
        from_email='ein3.14pi@gmail.com',
        recipient_list=[()]
    )