import json
# import simplejson
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.views.generic import (
    FormView, CreateView, UpdateView,
    DeleteView, ListView, DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from mainapp.models import Category, Product
from mainapp.forms import CategoryForm, CategoryModelForm


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


class CategoryGenericCreate(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'create.html'
    success_url = reverse_lazy('products:catalog')
    login_url = reverse_lazy('auth:login')


class CategoryGenericUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'create.html'
    success_url = reverse_lazy('products:catalog')
    slug_field = 'name'


class CategoryDetail(DetailView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'mainapp/components/categories.html'
    context_object_name = 'category'
    slug_field = 'name'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object.id)
        return context


class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'delete.html'
    success_url = reverse_lazy('products:catalog')
    slug_field = 'name'


# def category_detail(request, slug):
#     cat = Category.objects.get(title=slug)
#     products = Product.objects.filter(category=cat.id)
#     return render(request, 'mainapp/components/categories.html',
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