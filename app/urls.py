from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path('login/',LoginView.as_view(),name='login_user'),
    path('register/',SignUpView.as_view(),name='register_user'),
    # path('logout/',LogOutView.as_view(),name='logout_user'),
    path("update/",UserUpdateView.as_view(),name="update_user"),
    path("delete/",UserDeleteView.as_view(),name="delete_user"),
    path("get_user/",get_user_by_token.as_view(),name="get_user"),
]
