import json
# import simplejson
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.db import models
from django.views.generic import (
    FormView, CreateView, UpdateView,
    DeleteView, ListView, DetailView,
)
from mainapp.models import Category, Product
from mainapp.forms import CategoryForm, CategoryModelForm
from django.contrib.auth.decorators import user_passes_test
from mainapp.mixins import SuperUserMixin

# class CategoryCreate(View):
#     success_url = reverse_lazy('products:catalog')
#
#     def get(self, request):
#         form = CategoryForm()
#         return render(request, 'create.html', {'form': form})
#
#     def post(self, request):
#         form = CategoryForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             # return redirect('/')
#             return redirect(self.success_url)
#         return render(request, 'create.html', {'form': form})


class CategoryGenericCreate(SuperUserMixin, CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'create.html'
    success_url = reverse_lazy('products:catalog')

    def get_context_data(self, **kwargs):
        context = super(CategoryGenericCreate, self).get_context_data(**kwargs)
        context['title'] = 'Создание категории'
        context['url_cancel'] = 'products:catalog'
        context['OK_text'] = 'Создать категорию'
        return context


class CategoryGenericUpdate(SuperUserMixin, UpdateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'create.html'
    success_url = reverse_lazy('products:catalog')
    slug_field = 'name'

    def get_context_data(self, **kwargs):
        context = super(CategoryGenericUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование категории'
        context['url_cancel'] = 'products:catalog'
        context['OK_text'] = 'Сохранить'
        return context


class CategoryDetail(SuperUserMixin, DetailView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'mainapp/categories.html'
    context_object_name = 'category'
    slug_field = 'name'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object.id)
        context['min_price'] = context['products'].aggregate(models.Min('price'))['price__min']
        context['max_price'] = context['products'].aggregate(models.Max('price'))['price__max']
        print(context['min_price'])
        return context




# class CategoryDelete(DeleteView):
#     model = Category
#     template_name = 'delete.html'
#     success_url = reverse_lazy('products:catalog')
#     slug_field = 'name'


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, title):
    category = get_object_or_404(Category, name=title)
    content = {'object_to_delete': category, 'title': 'Удаление категории', 'subject': 'категории',
               'name': category.name, 'part_name': 'Архив', 'url_cancel': request.META.get('HTTP_REFERER',
                                                                                           'products:catalog')}
    print(request.META.get('HTTP_REFERER', '/'))
    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('products:catalog'))
    return render(request, 'delete.html', content)


# def category_detail(request, slug):
#     cat = Category.objects.get(title=slug)
#     products = Product.objects.filter(category=cat.id)
#     return render(request, 'mainapp/categories.html',
#                   {'category': cat})

# def category_create(request):
#     form = CategoryForm(request.POST)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             short_desc = form.cleaned_data.get('short_desc')
#             desc = form.cleaned_data.get('desc')
#
#         Category.objects.create(
#             name=name,
#             short_desc=short_desc,
#             desc=desc
#         )
#
#     return render(request, 'create.html', {'form': form})