from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path('register/',SignUpView.as_view()),
    path("update/",UserUpdateView.as_view(),name="for-update")
]
