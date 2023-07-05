from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, ImageUploadForm, UserProfileForm
from .models import UserModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib import messages


def img_delete(request, id):
    user = UserModel.objects.get(id=id)
    user.user_img = 'icon/user_icon.png'
    user.save()
    return redirect('profile')

def img_upload(request):
    if request.method == "POST":
        form = ImageUploadForm(data=request.POST, files=request.FILES)
        # print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = UserModel.objects.get(username=request.user)
            user.user_img = form.cleaned_data['user_img']
            user.save()
            return redirect('profile')
    return render(request, 'main/profile.html')


def profile_view(request):
    user = UserModel.objects.get(username=request.user)
    if request.method == "POST":
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return redirect('profile')
    return render(request, 'main/profile.html', context={
        'user': user
    })


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.info(request, f"{user.username} Xush kelibsiz !")
                return redirect('todo_list')
            form.add_error('password', 'Parol yoki Username xato !')
    return render(request, 'main/login.html', context={
        'login_form': form
    })


def registration_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = UserModel(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password'])
            )
            user.save()
            messages.success(request, "Tabriklaymiz siz muvoffaqiyatli ro'yxatdan o'tdingiz.")
            return redirect('login')
    return render(request, 'main/registration.html', context={
        'registration_form': form
    })
