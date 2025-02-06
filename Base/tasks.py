from celery import shared_task
import time
from datetime import date, timedelta

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Category, Post, Subscribers, PostCategory


@shared_task
def weekly_news():

    today = date.today()
    start_week = today - timedelta(days=7)

    for i in Category.objects.all():
        category_posts = Post.objects.filter(created_time__range=[start_week, today], category=i)
        user_emails = Subscribers.objects.filter(category=i).values_list('user__email', flat=True)

        html_content = render_to_string(
            'weekly_news.html',
            {
                'posts': category_posts,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'Weekly news in {i}',
            body='Nani',
            from_email='ein3.14pi@gmail.com',
            to=user_emails,
    )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

@shared_task
def notify_news_creation(post_pk):
    post = Post.objects.get(pk=post_pk)
    post_categories = post.category.all()
    subscribers_email = Subscribers.objects.filter(category__in=post_categories).values_list('user__email', flat=True)

    html_content = render_to_string(
        'category_update.html',
        {
            'post': post,
        }
    )

    msg = EmailMultiAlternatives(
        subject=f'New post: {post.title}',
        body='Nani',
        from_email='ein3.14pi@gmail.com',
        to=subscribers_email,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
