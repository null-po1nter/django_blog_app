from django.urls import path
from django.contrib.auth import urls
from .views import SignUp


app_name = 'users'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup')
]
