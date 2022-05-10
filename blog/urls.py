from django.urls import path
from .views import post_list, post_detail, add_post

app_name = 'blog'

urlpatterns = [
    path('add_post/', add_post, name='add_post'),
    path('<slug:post>/', post_detail, name='post_detail'),
    path('', post_list, name='post_list'),
]
