from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        likes = 0
        for i in self.post_set.all().values('rating'):
            likes += i['rating'] * 3
        for i in self.user.comment_set.all().values('rating'):
            likes += i['rating']
        for i in self.post_set.all():
            for y in i.comment_set.all().values("rating"):
                likes += y['rating']
        self.rating = likes
        self.save()
    
    def __str__(self):
        return self.user.username.title()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return self.name.title()


class Post(models.Model):
    news = "N"
    article = "A"

    post_types = [
        (news, "news"),
        (article, "article")
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=1, choices=post_types)
    created_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def preview(self):
        return self.text[:124] + "..."

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.title.title()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title.title()} - {self.category.name.title()}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.text[30]
    
class Subscribers(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
