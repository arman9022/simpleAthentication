from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import RegisteForm, Edit_RegisteForm
from django.contrib.auth.views import PasswordChangeForm

def home(request):
	return render(request, 'home/home.html')

def about(request):
	return render(request, 'home/about.html')

def login_user(request):
	if request.method == "POST":
		username=request.POST ['username']
		password=request.POST ['password']
		user=authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, 'Login Successfully')
			return redirect ('home')
		else:
			messages.success(request, 'Try Again')
			return redirect ('login')
	else:		
		return render(request, 'auths/login.html')

def logout_user(request):
	logout(request)
	messages.success(request, 'Logout Successfully')
	return redirect ('login')	

def register_view(request):
	if request.method == "POST":
		form=RegisteForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data ['username']
			password=form.cleaned_data ['password1']
			user=authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, 'Create Successfully')
			return redirect ('home')
	else:
		form=RegisteForm()
	context={
		'form':form
	}
	return render(request, 'register/register.html', context)

def edit_register_view(request):
	if request.method == "POST":
		form=Edit_RegisteForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Create Successfully')
			return redirect ('home')
	else:
		form=Edit_RegisteForm(instance=request.user)
	context={
		'form':form
	}
	return render(request, 'register/edit_register.html', context)

def change_password_view(request):
	if request.method == "POST":
		form=PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, 'Change Password')
			return redirect ('home')
	else:
		form=PasswordChangeForm(user=request.user)
	context={
		'form':form
	}
	return render(request, 'password/change_password.html', context)
