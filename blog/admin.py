from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'slug', 'author', 'created_at', 'updated_at', 'published_at', 'is_published', 'tags')
    search_fields = ('title', 'content', 'author', 'category')
    list_filter = ('author', 'created_at', 'updated_at', 'published_at', 'is_published', 'tags', 'category')
    list_display_links = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_at'
    ordering = ('published_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    list_display_links = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('title',)
