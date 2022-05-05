from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.published.all()

    return render(request, 'index.html', context={
        'posts': posts,
    })


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, is_published=True)
    
    return render(request, 'post_detail.html', context={
        'post': post
    })
