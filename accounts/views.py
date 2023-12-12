# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def user_info(request):
    return render(request, 'registration/user_info.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
