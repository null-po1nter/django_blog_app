from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pytils.translit import slugify
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post
from .forms import PostForm


def post_list(request, tag=None, category=None):
    if tag:
        posts = Post.published.filter(tags__name__in=[tag])

    else:
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


@login_required
@permission_required('blog.add_post')
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.slug = slugify(request.POST.get('title'), )
            post.save()
            form.save_m2m()

            return redirect(
                post.get_absolute_url(),
                context={
                    'post': post
                }
            )
    
    else:
        form = PostForm()
    
    return render(request, 'post_edit.html', context={
        'form': form
    })


def posts_by_category(request, category):
    posts = Post.published.filter(category__title=category)

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
