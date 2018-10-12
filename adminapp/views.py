from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import (
    FormView, CreateView, UpdateView,
    DeleteView, ListView, DetailView,
)

from userapp.models import ShopUser
from mainapp.models import Category, Product
from userapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from adminapp.forms import ShopUserAdminEditForm


def admin_page(request):
    return render(request, 'adminapp/admin.html', {})


# def users(request):
#     users_list = ShopUser.objects.all().order_by('-is_active', \
#                                                  '-is_superuser', '-is_staff', 'username')
#     content = {
#         'objects': users_list
#     }
#     return render(request, 'adminapp/users.html', content)

# Модель User. CRUD
class UserList(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super(UserList, self).get_context_data(**kwargs)
        context['objects'] = ShopUser.objects.all().order_by('-is_active', \
                                                             '-is_superuser', '-is_staff', 'username')
        return context


def user_create(request):
    return HttpResponseRedirect('/')



# def user_create(request):
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#     if user_form.is_valid():
#         user_form.save()
#         return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#         content = {'update_form': user_form}
#         return render(request, 'adminapp/user_update.html', content)


class UserCreate(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')


class UserUpdate(UpdateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')
    slug_field = 'username'


# class UserDelete(DeleteView):
#     model = ShopUser
#     template_name = 'adminapp/user_delete.html'
#     success_url = reverse_lazy('admin:users')
#     slug_field = 'name'


def user_delete (request, title):
    user = get_object_or_404(ShopUser, username=title)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))
    content = {'user_to_delete': user}
    return render(request, 'adminapp/user_delete.html', content)


def user_update(request, title):
    return HttpResponseRedirect('/')


def user_delete(request, title):
    return HttpResponseRedirect('/')


# class ProductGenericUpdate(UpdateView):
#     model = Product
#     form_class = ProductModelForm
#     template_name = 'create.html'
#     success_url = reverse_lazy('products:catalog')

# Модель Category. CRUD
class CategoryList(ListView):
    model = Category
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'


# def categories (request):
#     title = 'админка/категории'
#     categories_list = ProductCategory.objects.all()
#     content = {
#     'title' : title,
#     'objects' : categories_list
#     }
#     return render(request, 'adminapp/categories.html' , content)


def category_create(request):
    pass


def category_update(request, title):
    pass


def category_delete(request, title):
    pass


# Модель Product. CRUD
class ProductList(ListView):
    model = Product
    template_name = 'adminapp/product_list.html'
    context_object_name = 'objects'


def products(request, title):
    category = get_object_or_404(Category, name=title)
    products_list = Product.objects.filter(category__name=title).order_by('name')
    content = {
        'category': category,
        'objects': products_list,
    }
    return render(request, 'adminapp/products.html', content)


def product_create(request, title):
    pass


def product_read(request, title):
    pass


def product_update(request, title):
    pass


def product_delete(request, title):
    pass
