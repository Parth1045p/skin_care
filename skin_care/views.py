from django.shortcuts import render,redirect
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
# from .models import User
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
  return render(request,'skin_care/base.html')

def register_page(request):
	if request.method=='POST':
	
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		confirm_password=request.POST['password1']
		if password==confirm_password:
			if User.objects.filter(username=username).exists():
				return redirect('regi')
			else:
				if User.objects.filter(email=email).exists():
					return redirect('regi')
				else:
					user=User.objects.create_user(username=username,email=email,password=password)
					auth.login(request,user)
					user.save()
					return redirect('logi')
		
	else:
		# return render(request,'skin_care/register.html')
		return render(request,'skin_care/register.html')

# else:

# 	return render(request,'skin_care/register.html')

def login_page(request):
	if request.method=='POST':
		Username=request.POST['username']
		Password=request.POST['password']

		user=auth.authenticate(username=Username,password=Password)

		if user is not None:
			auth.login(request,user)
			return redirect('dash')
		else:
			return redirect('logi')
	return render(request,'skin_care/login.html')

def dash_board(request):
	
	return render(request,'skin_care/dashboard.html')

def log_out(request):
	if request.method=='POST':
		auth.logout(request)
		return redirect('homi')
	return redirect('homi')

# def registerUser(request):
	# if request.method == 'POST':
	# 	username = request.POST['username']
	# 	email = request.POST['email']
	# 	password = request.POST['password']
	# 	password = make_password(password)

	# 	a = User(username=username, email=email, password=password)
	# 	a.save()
	# 	messages.success(request, 'Account Was Created Successfully')
	# 	return redirect('regi')
	# else:
	# 	messages.error(request, 'Failed To Register, Try Again Later')
	# 	return redirect('regi')