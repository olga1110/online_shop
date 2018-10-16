from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import (
    FormView, CreateView, UpdateView,
    DeleteView, ListView, DetailView,
)
from django.contrib.auth.decorators import user_passes_test

from userapp.models import ShopUser
from mainapp.models import Category, Product
from userapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from adminapp.forms import ShopUserAdminEditForm, CategoryEditForm, ProductEditForm


@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    return render(request, 'adminapp/admin.html', {})


# def users(request):
#     users_list = ShopUser.objects.all().order_by('-is_active', \
#                                                  '-is_superuser', '-is_staff', 'username')
#     content = {
#         'objects': users_list
#     }
#     return render(request, 'adminapp/users.html', content)

# CDUD-методы. Пользователи
class UserList(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super(UserList, self).get_context_data(**kwargs)
        context['objects'] = ShopUser.objects.all().order_by('-is_active', \
                                                             '-is_superuser', '-is_staff', 'username')
        return context


# def user_create(request):
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#     if user_form.is_valid():
#         user_form.save()
#         return HttpResponseRedirect(reverse('admin_custom:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#         content = {'update_form': user_form}
#         return render(request, 'adminapp/update.html', content)


class UserCreate(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/update.html'
    success_url = reverse_lazy('admin_custom:users')


class UserUpdate(UpdateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    template_name = 'adminapp/update.html'
    success_url = reverse_lazy('admin_custom:users')
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        context = super(UserUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Добавление пользователя'
        context['return'] = 'К списку пользователей'
        return_path = self.request.META.get('HTTP_REFERER', '/')
        context['url_name'] = return_path
        context['url_form'] = 'admin_custom:users'
        context['url_arg'] = ''
        return context


def user_delete(request, title):
    user = get_object_or_404(ShopUser, username=title)
    content = {'object_to_delete': user, 'title': 'Удаление пользователя', 'subject': 'пользователя',
               'name': user.username, 'part_name': 'Заблокированные пользователи',
               'url_cancel': 'admin_custom:users'}
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect("/admin_custom/users/")
    return render(request, 'adminapp/delete.html', content)


# CDUD-методы. Категории
class CategoryList(ListView):
    model = Category
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'


class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryEditForm
    template_name = 'adminapp/update.html'
    success_url = reverse_lazy('admin_custom:category')
    slug_field = 'name'

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование категории'
        context['return'] = 'К списку категорий'
        return_path = self.request.META.get('HTTP_REFERER', '/')
        context['url_name'] = return_path
        context['url_form'] = 'admin_custom:products'
        context['url_arg'] = self.object.name

        return context


class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryEditForm
    template_name = 'adminapp/update.html'
    success_url = reverse_lazy('admin_custom:catalog')


def category_delete(request, title):
    category = get_object_or_404(Category, name=title)
    content = {'object_to_delete': category, 'title': 'Удаление категории', 'subject': 'категории',
               'name': category.name, 'part_name': 'Архив', 'url_cancel': 'admin_custom:category'}
    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect("/admin_custom/catalog/")
    return render(request, 'adminapp/delete.html', content)


# class UserDelete(DeleteView):
#     model = ShopUser
#     template_name = 'adminapp/user_delete.html'
#     success_url = reverse_lazy('admin_custom:users')
#     slug_field = 'name'


# class ProductGenericUpdate(UpdateView):
#     model = Product
#     form_class = ProductModelForm
#     template_name = 'create.html'
#     success_url = reverse_lazy('products:catalog')

# Модель Category. CRUD


# def categories (request):
#     title = 'админка/категории'
#     categories_list = ProductCategory.objects.all()
#     content = {
#     'title' : title,
#     'objects' : categories_list
#     }
#     return render(request, 'adminapp/categories.html' , content)


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


class ProductCreate(CreateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/update.html'
    success_url = reverse_lazy('admin_custom:products')


def product_read(request, title):
    pass


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/update.html'
    success_url = reverse_lazy('admin_custom:product_list')
    slug_field = 'name'

    def get_context_data(self, **kwargs):
        context = super(ProductUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование товара'
        context['return'] = 'К списку товаров'
        return_path = self.request.META.get('HTTP_REFERER', '/')
        context['url_name'] = return_path
        context['url_form'] = 'admin_custom:products'
        context['url_arg'] = self.object.category.name
        return context


def product_delete(request, title):
    product = get_object_or_404(Product, name=title)
    content = {'object_to_delete': product, 'title': 'Удаление товара', 'subject': 'товара',
               'name': product.name, 'part_name': 'Архив', 'url_cancel': 'admin_custom:product_list'}
    if request.method == 'POST':
        product.is_active = False
        product.save()
        # return HttpResponseRedirect(request.META["HTTP_REFERER"])
        return HttpResponseRedirect("/admin_custom/products/category/"+product.category.name)
    return render(request, 'adminapp/delete.html', content)


