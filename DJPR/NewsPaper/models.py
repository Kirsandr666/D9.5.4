from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        author_posts_rating = Post.objects.all().filter(author_id=self.pk).aggregate(
            posts_rating_sum=Sum('rating') * 3)
        author_comments_rating = Comment.objects.all().filter(user_id=self.user).aggregate(
            comments_rating_sum=Sum('rating_com'))

        print(author_posts_rating)
        print(author_comments_rating)

        self.author_rating = author_posts_rating['posts_rating_sum'] + author_comments_rating['comments_rating_sum']
        self.save()


politics = 'PO'
art = 'AR'
show = 'SH'
rest = 'RS'

TOPICS = [
    (politics, 'ПОЛИТИКА'),
    (art, 'ИСКУССТВО'),
    (show, 'Шоу-бизнес'),
    (rest, 'Досуг')
]


class Category(models.Model):
    topic = models.CharField(max_length=2, choices=TOPICS, default=politics, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return self.topic.title()


class Post(models.Model):
    ART = 'С'
    NEWS = 'Н'

    TYPES = [(ART, 'Статья'), (NEWS, 'Новость')]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=15, choices=TYPES)
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=120)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:125] + '...'

    def __str__(self):
        return f'{self.title.title()}:{self.text.title()}:{self.date_in}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=255)
    created_com = models.DateTimeField(auto_now_add=True)
    rating_com = models.IntegerField(default=0)

    def like(self):
        self.rating_com += 1
        self.save()

    def dislike(self):
        self.rating_com -= 1
        self.save()

