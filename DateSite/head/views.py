# import requests
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout
from .forms import *
from django.contrib.auth.decorators import login_required

def home(request):
    action = request.GET.get('action')
    confirm_login = False
    if action == 'log_in':
        confirm_login = True
    form = SignInForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('head:profile', pk=user.pk)
    return render(request, 'home.html', {'form': form, 'confirm_login': confirm_login})


@login_required(login_url='/head/home/')
def profile(request, pk):
    account = Profile.objects.get(user__pk=pk)
    return render(request, 'profile.html', {'account': account})


@login_required(login_url='/head/home/')
def edit_photo(request, pk):
    account = Profile.objects.get(user__pk=pk)
    form = PhotoProfileForm(request.POST or None,
                            request.FILES or None,
                            instance=account)

    if request.user != account.user:
        return render(request, 'error.html')
    
    action = request.GET.get('action')
    confirm_photo = False

    if action == 'photo':
        confirm_photo = True
        if form.is_valid():
            form.save()
            return redirect('head:profile', pk=request.user.pk)
    if action == 'delete':
        account.image = 'default-profile-photo.png'
        account.save()
        
    return render(request, 'profile.html', {'account': account, 'form': form, 'confirm_photo': confirm_photo})


@login_required(login_url='/head/home/')
def edit_about(request, pk):
    account = Profile.objects.get(user__pk=pk)
    if request.user !=account.user:
        return render(request, 'error.html')
    about_me_form = AboutMeProfileForm(request.POST or None, instance=account)
    action = request.GET.get('action')
    confirm_about = False

    if action == 'about_me':
        confirm_about = True
        if about_me_form.is_valid():
            account.save()
            return redirect('head:profile', pk=request.user.pk)

    return render(request, 'profile.html',
                  {'account': account, 'about_me_form': about_me_form, 'confirm_about': confirm_about})


@login_required(login_url='/head/home/')
def photo(request, pk):
    action = request.GET.get('action')
    confirm = False
    account = Profile.objects.get(user__pk=pk)
    if request.user != account.user:
        return render(request, 'error.html')
    
    form = UploadPhotoForm(request.POST or None, request.FILES or None)
    if action == 'add_photo':
        confirm = True
        if form.is_valid():
            data_photo = MyPhoto.objects.create(profile=account)
            data_photo.photo=request.FILES['photo']
            data_photo.save()
            return redirect('head:photo', pk=request.user.pk)
    photos = account.my_photos.all()
    
    return render(request, 'photo.html', {'account': account, 'form': form, 'photos': photos ,'confirm': confirm})

@login_required(login_url='/head/home/')
def delete_photo(request, pk):
    my_photo_data = MyPhoto.objects.get(pk=pk)
    if request.user != my_photo_data.profile.user:
        return render(request, 'error.html')
    
    if request.method == 'POST':
        MyPhoto.objects.get(pk=pk).delete()
        return redirect('head:photo', pk=request.user.pk)
    return render(request, 'delete_photo.html', {'my_photo_data': my_photo_data}) # , 'photos': all_photos 'confirm_ph': confirm_ph


@login_required(login_url='/head/home/')
def settings(request, pk):
    account = Profile.objects.get(user__pk=pk)
    if request.user != account.user:
        return render(request, 'error.html')
    username_form = UserForm(data=request.POST or None, instance=account.user)
    form = EditProfileForm(data=request.POST or None, instance=account)
    if form.is_valid() and username_form.is_valid():
        username_form.save()
        account.user.username = username_form.data['username']
        form.save()
        account.age = form.data['age']
        account.city = form.data['city']
        account.job = form.data['job']
        account.hobbies = form.data['hobbies']
        account.status = form.data['status']
        account.gender = form.data['gender']
        return redirect('head:profile', pk=request.user.pk)
    return render(request, 'settings.html', {'form': form, 'usernameform': username_form,'account': account}) # 


@login_required(login_url='/head/home/')
def search(request):
    account = Profile.objects.get(user__pk=request.user.pk)
    form = SearchForm(request.POST or None)
    profiles = []
    if request.method == 'POST':
        if form.is_valid():
            
            gender = form.data['gender']
            age_min = form.data['age_min'] if form.data['age_min'] else 18
            age_max = form.data['age_max'] if form.data['age_max'] else 99
            city = form.data['city'] if form.data['city'] else None

            if city:
                q_profiles = list(Profile.objects.filter(
                    gender=gender,
                    age__in=range(int(age_min), int(age_max) + 1),
                    city=city
                ))
                t_profiles = list(Profile.objects.filter(
                    gender=gender, 
                    age=None,
                    city=city
                ))
                if (form.data['age_min'] or form.data['age_max']):
                    profiles = q_profiles
                else:
                    profiles=q_profiles+t_profiles
            else:
                q_profiles = list(Profile.objects.filter(
                    gender=gender,
                    age__in=range(int(age_min), int(age_max) + 1)
                ))
                t_profiles = list(Profile.objects.filter(
                    gender=gender, 
                    age=None
                ))
                if (form.data['age_min'] or form.data['age_max']):
                    profiles = q_profiles
                else:
                    profiles=q_profiles+t_profiles
            
    print(profiles)
    return render(request, 'search.html', {'account': account, 'form': form, 'profiles': profiles})



def sign_out(request):
    logout(request)
    return redirect('head:home')
