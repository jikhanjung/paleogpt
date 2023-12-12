# accounts/urls.py
from django.urls import path

#from .views import SignUpView
from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("logout_view/", views.logout_view, name="logout_view"),
]