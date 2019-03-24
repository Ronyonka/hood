from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *


# @login_required
def home(request):
   user = request.user
   return render(request, 'home.html',{'user':user})

def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('edit_profile')

    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html',{'form':form})

@login_required
def edit_profile(request):

   user = request.user

   if request.method == 'POST':
      form = ProfileUpdateForm(request.POST,request.FILES,instance=user.profile)
      user_form = UserUpdateForm(request.POST,instance=user)
      if user_form.is_valid() and form.is_valid():
         user_form.save()
         profile = form.save(commit=False)
         profile.user = user
         profile.save()
         messages.info(request, 'You\'ve successfully updated your account!')
         return redirect('home')
   else:
      form = ProfileUpdateForm(instance=request.user)
      user_form = UserUpdateForm(instance=request.user.profile)

   context = { 
      'user': user,
      'user_form': user_form,
      'form': form
   }

   return render(request, 'edit-profile.html', context)