from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


def post_list(request):
    posts = Post.published.all()

    # pagination
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    
    except PageNotAnInteger:            # if page is not an integer
        posts = paginator.page(1)       # deliver the first page
   
    except EmptyPage:                                   # if page is out of range
        posts = paginator.page(paginator.num_pages)     # deliver last page of results

    return render(request, 'index.html', context={
        'posts': posts,
        page: 'pages',          # pass the page number
    })


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, is_published=True)
       
    return render(request, 'post_detail.html', context={
        'post': post,
    })
