from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import (
    FormView, CreateView, UpdateView,
    DeleteView, ListView, DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test

from userapp.models import ShopUser
from mainapp.models import Category, Product
from userapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from adminapp.forms import ShopUserAdminEditForm, CategoryEditForm, ProductEditForm
from mainapp.forms import ProductModelForm
from django.contrib import messages
from adminapp.mixins import SuperUserMixin


@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    return render(request, 'adminapp/admin.html', {})


# CDUD-методы. Пользователи
class UserList(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'
    paginate_by = 2

    def get_queryset(self):
        queryset = ShopUser.objects.all().order_by('-is_active',
                                                   '-is_superuser', '-is_staff', 'username')
        return queryset


class UserCreate(LoginRequiredMixin, SuperUserMixin, CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'create.html'
    success_url = reverse_lazy('admin_custom:users')
    handle_no_permission = '/auth/login/'

    def get_context_data(self, **kwargs):
        context = super(UserCreate, self).get_context_data(**kwargs)
        context['title'] = 'Создание пользователя'
        context['url_cancel'] = 'admin_custom:users'
        context['OK_text'] = 'Создать'
        return context


class UserUpdate(LoginRequiredMixin, SuperUserMixin, UpdateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    template_name = 'create.html'
    success_url = reverse_lazy('admin_custom:users')
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        context = super(UserUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование пользователя'
        context['OK_text'] = 'Сохранить'
        context['url_cancel'] = 'admin_custom:users'
        return context


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, title):
    user = get_object_or_404(ShopUser, username=title)
    content = {'object_to_delete': user, 'title': 'Удаление пользователя', 'subject': 'пользователя',
               'name': user.username, 'part_name': 'Заблокированные пользователи',
               'url_cancel': request.META.get('HTTP_REFERER', 'admin_custom:users')}
    print(request.resolver_match.app_name)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect("/admin_custom/users/")
    return render(request, 'delete.html', content)


# CDUD-методы. Категории

class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'
    paginate_by = 2


class CategoryCreate(LoginRequiredMixin, SuperUserMixin, CreateView):
    model = Category
    form_class = CategoryEditForm
    template_name = 'create.html'
    success_url = reverse_lazy('admin_custom:category')

    def get_context_data(self, **kwargs):
        context = super(CategoryCreate, self).get_context_data(**kwargs)
        context['title'] = 'Создание категории'
        context['url_cancel'] = 'admin_custom:category'
        context['OK_text'] = 'Создать'
        return context


class CategoryUpdate(LoginRequiredMixin, SuperUserMixin, UpdateView):
    model = Category
    form_class = CategoryEditForm
    template_name = 'create.html'
    success_url = reverse_lazy('admin_custom:category')
    slug_field = 'name'

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование категории'
        context['OK_text'] = 'Сохранить'
        context['url_cancel'] = 'admin_custom:category'
        return context


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, title):
    category = get_object_or_404(Category, name=title)
    content = {'object_to_delete': category, 'title': 'Удаление категории', 'subject': 'категории',
               'name': category.name, 'part_name': 'Архив', 'url_cancel': request.META.get('HTTP_REFERER',
                                                                                           'admin_custom:category')}
    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'delete.html', content)


# Модель Product. CRUD


class ProductList(ListView):
    model = Product
    template_name = 'adminapp/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        # context['categories'] = Category.objects.all().order_by('name')
        context['active_categories'] = Category.objects.filter(id__in=Product.objects.filter(is_active=1).
                                                               values('category')).order_by('name')
        context['archive_categories'] = Category.objects.filter(id__in=Product.objects.filter(is_active=0).
                                                                values('category')).order_by('name')
        # Category.objects.filter(id__in=Product.objects.filter(is_active=1).values('category')).order_by('name')
        return context

    def get_queryset(self):
        queryset = Product.objects.all().order_by('category_id', 'price')
        return queryset


class ProductCategory(ListView):
    model = Product
    template_name = 'adminapp/products_category.html'
    context_object_name = 'products'
    slug_field = 'name'
    paginate_by = 2

    def get_queryset(self):
        queryset = Product.objects.filter(category__name=self.kwargs['slug']).order_by('price', 'name')
        return queryset


def products(request, title):
    category = get_object_or_404(Category, name=title)
    products_list = Product.objects.filter(category__name=title).order_by('name')
    content = {
        'category': category,
        'objects': products_list,
    }
    return render(request, 'adminapp/product_list.html', content)


class ProductCreate(LoginRequiredMixin, SuperUserMixin, CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'create.html'
    success_url = reverse_lazy('admin_custom:product_list')

    def get_context_data(self, **kwargs):
        context = super(ProductCreate, self).get_context_data(**kwargs)
        context['title'] = 'Создание товара'
        context['url_cancel'] = 'admin_custom:product_list'
        context['OK_text'] = 'Добавить товар'
        return context


class ProductUpdate(LoginRequiredMixin, SuperUserMixin, UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'create.html'
    success_url = reverse_lazy('admin_custom:product_list')
    slug_field = 'name'

    def get_context_data(self, **kwargs):
        context = super(ProductUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование товара'
        context['OK_text'] = 'Сохранить'
        context['url_cancel'] = 'admin_custom:product_list'
        return context


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, title):
    product = get_object_or_404(Product, name=title)
    content = {'object_to_delete': product, 'title': 'Удаление товара', 'subject': 'товара',
               'name': product.name, 'part_name': 'Архив', 'url_cancel': request.META.get('HTTP_REFERER',
                                                                                          'admin_custom:product_list')}
    if request.method == 'POST':
        product.is_active = False
        product.save()
        # return HttpResponseRedirect(request.META["HTTP_REFERER"])
        return HttpResponseRedirect("/admin_custom/products/category/" + product.category.name)
    return render(request, 'delete.html', content)

# def users(request):
#     users_list = ShopUser.objects.all().order_by('-is_active', \
#                                                  '-is_superuser', '-is_staff', 'username')
#     content = {
#         'objects': users_list
#     }
#     return render(request, 'adminapp/users.html', content)

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

# def get_absolute_url(self):
#     # return reverse('admin_custom:products', kwargs={'title': self.model.category.name})
#     print(self.model.category.name)
#     return reverse('products', kwargs={'title': self.form_class.category.name})
