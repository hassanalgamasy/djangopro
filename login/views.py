from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from accounts.models import User

# Create your views here.

def login_view(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid() :
            username_or_phone=form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user=User.objects.get(username=username_or_phone)
            except User.DoesNotExist:
                try:
                    user=User.objects.get(phone=username_or_phone)
                except User.DoesNotExist:
                    user = None
            if user is not None:
                authenticated_user=authenticate(request, username=user.username, password=password)
                if authenticated_user is not None:
                    login(request,authenticated_user)
                    if authenticated_user.account_type=='client':
                        return redirect('client_dashboard')
                    elif authenticated_user.account_type == 'company':
                        return redirect('company_dashboard')
                else:
                    messages.error(request, "كلمه المرور غير صحيحه ")
            else:
                messages.error(request, 'هذا المستخدم غير موجود')
    else:
        form=LoginForm
    return render (request, 'login/login.html', {'form':form})