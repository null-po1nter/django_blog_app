from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'slug', 'author', 'created_at', 'updated_at', 'published_at', 'is_published', 'tags')
    search_fields = ('title', 'content', 'author')
    list_filter = ('author', 'created_at', 'updated_at', 'published_at', 'is_published', 'tags')
    list_display_links = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_at'
    ordering = ('published_at',)
