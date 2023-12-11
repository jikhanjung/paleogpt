# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def user_info(request):
    return render(request, 'registration/user_info.html')

