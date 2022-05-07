from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


User = get_user_model()


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    slug = models.SlugField(max_length=200, unique_for_date='published_at')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    tags = TaggableManager(blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')

    published = PublishManager()

    class Meta:
        ordering = ('-published_at',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug])

    def __str__(self):
        return self.title
