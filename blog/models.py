from django.contrib.auth.models import User
from django.db import models as m
from django.urls import reverse
from django.utils import timezone


class PublishManager(m.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(m.Model):
    class Meta:
        ordering = ['-publish']
        indexes = [m.Index(fields=['-publish'])]

    class Status(m.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    posts = m.Manager()
    published = PublishManager()

    title = m.CharField(max_length=250)
    slug = m.SlugField(max_length=250, unique_for_date='publish')
    author = m.ForeignKey(User, on_delete=m.CASCADE, related_name='blog_posts')
    status = m.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    body = m.TextField()
    publish = m.DateTimeField(default=timezone.now)
    created = m.DateTimeField(auto_now_add=True)
    updated = m.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])