from django.shortcuts import render, redirect, HttpResponseRedirect
from userapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from userapp.models import ShopUser
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    FormView, CreateView, UpdateView,
    DeleteView, ListView, DetailView,
)
from userapp.mixins import AnonRequiredMixin


# def login(request):
#     login_form = ShopUserLoginForm(data=request.POST or None)
#     next = request.GET['next'] if 'next' in request.GET.keys() else ''
#     if request.method == 'POST' and login_form.is_valid():
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user and user.is_active:
#             auth.login(request, user)
#             if 'next' in request.POST.keys():
#                 return HttpResponseRedirect(request.POST['next'])
#             # return HttpResponseRedirect(reverse( 'main' ))
#             return HttpResponseRedirect('/')
#     content = {'login_form': login_form,
#                'next': next
#                }
#     return render(request, 'userapp/login.html', content)


class LoginView(AnonRequiredMixin, FormView):
    model = ShopUser
    form_class = ShopUserLoginForm
    template_name = 'userapp/login.html'
    success_url = reverse_lazy('products:catalog')

    def post(self, request, *args, **kwarg):
        form = self.form_class(data=request.POST or None)
        next = request.GET['next'] if 'next' in request.GET.keys() else ''

        if form.is_valid():
            usr = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = auth.authenticate(
                username=usr,
                password=pwd
            )

            if user and user.is_active:
                auth.login(request, user)
                if next:
                    return HttpResponseRedirect(next)
                return redirect(self.success_url)

        content = {'form': self.form_class,
                   'next': next
                   }

        return render(
            request,
            self.template_name,
            content
        )


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


class UserRegister(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'userapp/register.html'
    success_url = reverse_lazy('auth:login')


# def register(request):
#     if request.method == 'POST':
#         register_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if register_form.is_valid():
#             register_form.save()
#             return HttpResponseRedirect(reverse('auth:login'))
#     else:
#         register_form = ShopUserRegisterForm()
#         content = dict(register_form=register_form, next=next)
#         return render(request, 'userapp/register.html', content)


class UserEdit(UpdateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'userapp/register.html'
    success_url = reverse_lazy('auth:login')
    slug_field = 'username'

# def edit(request):
#     if request.method == 'POST':
#         edit_form = ShopUserEditForm(request.POST, request.FILES,
#                                      instance=request.user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('auth:edit'))
#     else:
#         edit_form = ShopUserEditForm(instance=request.user)
#     content = {'edit_form': edit_form}
#     return render(request, 'userapp/edit.html', content)
