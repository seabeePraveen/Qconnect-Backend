from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path('register/',SignUpView.as_view()),
    path("update/",UserUpdateView.as_view(),name="update_user"),
    path("delete/",UserDeleteView.as_view(),name="delete_user"),
    path("get_user/",get_user_by_token.as_view(),name="get_user"),
    path("get_messages",views.get_message,name="getting message")
]
