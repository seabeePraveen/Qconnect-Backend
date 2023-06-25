from django.urls import path
from . import views
import requests
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path("",views.home,name="home"),
    path("gettoken/",TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path("refreshtoken/",TokenRefreshView.as_view(),name="refresh_token"),
]
