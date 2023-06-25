from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import *


urlpatterns = [
    path("",views.home,name="home"),
    path("login/",LoginView.as_view()),
    path('register/', CustomUserCreateView.as_view(), name='register'),
]
