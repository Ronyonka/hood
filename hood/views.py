from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .forms import *


@login_required
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

@login_required
def own_profile(request):
   '''
   Directs Current User to their own Profile.
   '''
   user = request.user  
   hood = Hood.objects.all()
   profile = Profile.objects.all().filter(user=user)  
   buisnesses = Business.objects.all().filter(owner_id = user.id)
   posts = Posts.objects.all().filter(author=profile)

   return render(request, 'profile.html', {'businesses':buisnesses,'profile':profile, "user":user,"posts":posts, "hood":hood })

@login_required
def new_posts(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = profile
            posts.hood = profile.hood
            posts.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'add_posts.html', {"form":form})

@login_required
def posts(request):
   profile = Profile.objects.get(user = request.user)
   posts = Posts.objects.filter(hood = profile.hood)
   return render(request, 'posts.html',{'profile':profile,'posts':posts})

@login_required
def new_hood(request):
   if request.method == 'POST':
         form = LocationForm(request.POST,request.FILES)
         hood_form = HoodForm(request.POST,request.FILES)
         if form.is_valid() and hood_form.is_valid():
            location = form.save(commit=False)
            location.save()
            hood = hood_form.save(commit=False)
            hood.location = location
            hood.save()
            return redirect('home')
   else:
      form = LocationForm()
      hood_form = HoodForm()

   context = { 
      'hood_form': hood_form,
      'form': form
   }

   return render(request, 'new_hood.html', context)

@login_required(login_url='/accounts/login')
def search(request):
    if 'search' in request.GET and request.GET['search']:
        profile = Profile.objects.get(user = request.user)
        search_term = request.GET.get('search')
        businesses = Business.objects.filter(hood = profile.hood, name__icontains = search_term)
        message = f'{search_term}'
        context = {
            'message': message,
            'businesses': businesses
        }
        
    return render(request, 'search.html', context)

