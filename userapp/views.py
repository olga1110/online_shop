from django.shortcuts import render, HttpResponseRedirect
from userapp.forms import ShopUserLoginForm, ShopUserRegisterForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            # return HttpResponseRedirect(reverse( 'main' ))
            return HttpResponseRedirect('/')
    content = {'login_form': login_form}
    return render(request, 'userapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register(request):
    return HttpResponseRedirect('/')


def edit(request):
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()
        content = {'register_form': register_form}
        return render(request, 'userapp/register.html', content)
