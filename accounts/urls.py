# accounts/urls.py
from django.urls import path

#from .views import SignUpView
from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("user_info/", views.user_info, name="user_info"),
]