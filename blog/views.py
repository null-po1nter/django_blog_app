from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.published.all()

    return render(request, 'index.html', context={
        'posts': posts,
    })
