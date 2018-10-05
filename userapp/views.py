from django.shortcuts import render

from django.shortcuts import render, HttpResponseRedirect
from userapp.forms import ShopUserLoginForm
from django.contrib import auth
from django.urls import reverse


from django.shortcuts import render, HttpResponseRedirect
from userapp.forms import ShopUserLoginForm
from django.contrib import auth
from django.urls import reverse

def login (request):
    title = 'вход'
    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST[ 'username' ]
        password = request.POST[ 'password' ]
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse( 'main' ))
    content = { 'title' : title, 'login_form' : login_form}
    return render(request, 'userapp/login.html' , content)

def logout (request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
