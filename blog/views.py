from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
from .models import Post, Category



def post_list(request):
    posts = Post.published.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'index.html', context={
        'posts': posts,
        'categories': categories,
        'tags': tags
    })


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, is_published=True)
    
    return render(request, 'post_detail.html', context={
        'post': post,
    })
