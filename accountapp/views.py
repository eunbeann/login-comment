from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django. contrib import auth

# Create your views here.
def main(request):
    return render(request, 'main.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')