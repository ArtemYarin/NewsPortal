from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post, PostCategory, Subscribers


@receiver(m2m_changed, sender=PostCategory)
def notify_managers_news(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        post_categories = instance.category.all()
        subscribers_email = Subscribers.objects.filter(category__in=post_categories).values_list('user__email', flat=True)

        html_content = render_to_string(
            'category_update.html',
            {
                'post': instance,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'New post: {instance.title}',
            body='Nani',
            from_email='ein3.14pi@gmail.com',
            to=subscribers_email,
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
