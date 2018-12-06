from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import FormView
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from userapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from userapp.models import ShopUser


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


class LoginView(FormView):
    model = ShopUser
    form_class = ShopUserLoginForm
    template_name = 'userapp/login.html'
    success_url = reverse_lazy('products:start_page')

    def post(self, request, *args, **kwargs):
        next = request.GET['next'] if 'next' in request.GET.keys() else ''
        login_form = self.form_class(data=request.POST or None)

        if login_form.is_valid():
            usr = login_form.cleaned_data.get('username')
            pwd = login_form.cleaned_data.get('password')

            user = auth.authenticate(
                username=usr,
                password=pwd
            )

            if user and user.is_active:
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                auth.login(request, user)
                return redirect(self.success_url)
                # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return render(
            request,
            self.template_name,
            {'login_form': login_form,
             'next': next
             }
        )


def logout(request):
    auth.logout(request)
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


def edit(request):
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES,
                                     instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
    content = {'edit_form': edit_form}
    return render(request, 'userapp/edit.html', content)
