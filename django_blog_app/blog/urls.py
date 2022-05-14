from django.urls import path
from .views import post_list, add_post, post_detail, posts_by_tag


urlpatterns = [
    path('', post_list, name='index'),
    path('add_post/', add_post, name='add_post'),
    path('<slug:post>/', post_detail, name='post_detail'),
    path('tag/<str:tag>/', posts_by_tag, name='post_list')
]
