from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.urls import reverse





def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))
            return redirect('login')
    else:
        return render(request, 'user_auth/login.html', {})







def logout_user(request):
    logout(request)
    messages.success(request, "You Were Logged Out!")
    return redirect('home')


def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('home')
	else:
		form = RegisterUserForm()

	return render(request, 'user_auth/register_user.html', {
		'form':form,
		})




# def authenticate_user(request):
#     """
#     Function is used to authenticate the user.

#     :param request: data input from the website received via request

#     :return: directs user to appropriate page (if user is not found == register new user page; if user authenticated == home page)
#     """
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)

#     if user is None:
#         return HttpResponseRedirect(reverse('user_auth:register_user'))
#     else:
#         login(request,user)
#         return HttpResponseRedirect(reverse('website:home'))
	


    


