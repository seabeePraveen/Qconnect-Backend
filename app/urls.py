from django.urls import path
from .views import *

urlpatterns = [
    path('register/',SignUpView.as_view()),
]
