from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .forms import *


# @login_required
def home(request):
   hood = Hood.objects.all()
   profile = Profile.objects.get(user = request.user)
   buisnesses = Business.objects.filter(hood = profile.hood)
   return render(request, 'home.html',{'profile':profile,'hood':hood, 'businesses':buisnesses})

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

@login_required
def hood(request,id):
   user = request.user
   businesses = Business.get_business(id=id)

   return render(request,'hood.html',{'user':user,'businesses':businesses})

   
@login_required
def new_business(request):
    profile = Profile.objects.get(user = request.user)
    user= request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = profile
            business.hood = profile.hood
            business.save()
            return redirect('home')
    else:
        form = BusinessForm()

    return render(request, 'add_business.html', {"form":form})

@login_required
def business(request):
   profile = Profile.objects.get(user = request.user)
   buisnesses = Business.objects.filter(hood = profile.hood)
   return render(request, 'business.html',{'profile':profile, 'businesses':buisnesses})
