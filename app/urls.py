from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.home,name="home"),
    path('login/',LoginView.as_view(),name='login_user'),
    path('register/',SignUpView.as_view(),name='register_user'),
    # path('logout/',LogOutView.as_view(),name='logout_user'),
    path("update/",UserUpdateView.as_view(),name="update_user"),
    path("delete/",UserDeleteView.as_view(),name="delete_user"),
    path("get_user/",get_user_by_token.as_view(),name="get_user"),
    path("get_user_with_string/",get_users_by_starting_string.as_view(),name='get_user_with_string'),
    path("get_last_messages_of_user_and_details/",get_last_messages_of_user_and_details.as_view(),name="get_last_messages_of_user_and_details"),
    path("get_messages/",views.get_messages,name="getting messages of user2"),
    path("get/",GetMessagesUser1ToUser2.as_view(),name="getting of host and user2"),
    path("send/",SendingMessages.as_view(),name="sending messages"),
    path("change_password/",ChangePassword.as_view(),name="change password")

]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)