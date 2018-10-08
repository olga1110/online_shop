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


class CategoryGenericCreate(CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'create.html'
    success_url = reverse_lazy('products:catalog')


class CategoryGenericUpdate(UpdateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'create.html'
    success_url = reverse_lazy('products:catalog')


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


class CategoryDetail(DetailView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'mainapp/components/categories.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object.id)
        return context


# def category_detail(request, title):
#     cat = Category.objects.get(name=title)
def category_detail(request, pk):
    cat = Category.objects.get(id=pk)
    # products = Product.objects.filter(category=cat.id)
    products = Product.objects.filter(category=pk)
    return render(request, 'mainapp/components/categories.html',
                  {'category': cat})


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'delete.html'
    success_url = reverse_lazy('products:catalog')
