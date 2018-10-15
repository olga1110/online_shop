import os
import json
# import simplejson
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    FormView, CreateView, UpdateView,
    DeleteView, ListView, DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from mainapp.models import Product, Category
from mainapp.forms import ProductModelForm



def update_price_from_file(product):
    obj = Product.objects.get(name=product)

    path = 'mainapp/static/mainapp/files/description.json'
    with open(path) as json_data:
        data = json.load(json_data)

    obj.price = data['description'][product]
    obj.save()



def mainapp_Contacts(request):
    path = 'mainapp/static/mainapp/files/organization.json'
    with open(path) as json_data:
        context = json.load(json_data)

    template = get_template('mainapp/contacts.html')
    return HttpResponse(template.render(context))



def mainapp_index(request):
    context = {'company':
                   {'title': 'cozy kitchen',
                    'advertisement': 'Самая лучшая мебель для кухни здесь!!!'}
               }
    return render(request, 'mainapp/index.html', context)



def mainapp_registration(request):
    context = {'reg': 'Регистрация'}
    return render(request, 'mainapp/registration.html', context)


class ProductGenericCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'create.html'
    success_url = reverse_lazy('products:catalog')
    login_url = reverse_lazy('auth:login')


class ProductGenericUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'create.html'
    slug_field = 'name'
    success_url = reverse_lazy('products:catalog')
    login_url = reverse_lazy('auth:login')



# class ProductCreate(View):
#     template_name = 'create.html'
#     context_object_name = 'form'
#     success_url = reverse_lazy('products:catalog')
#
#
#     def get(self, request):
#         form = ProductModelForm()
#         return render(request, self.template_name, {self.context_object_name: form})
#
#     def post(self, request):
#         form = ProductModelForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect(self.success_url)
#         return render(request, self.template_name, {self.context_object_name: form})


# class ProductUpdate(FormView):
#     form_class = ProductModelForm
#     success_url = reverse_lazy('products:catalog')
#     template_name = 'create.html'
#     slug_field = 'name'
#
#     def post(self, request, title):
#         obj = get_object_or_404(Product, name=title)
#         form = self.form_class(
#             request.POST,
#             instance=obj
#         )
#         if form.is_valid():
#             form.save()
#             return redirect(self.success_url)
#         return render(request, self.template_name, {'form': form})


# @login_required(login_url=reverse_lazy('auth:login'))
def category_product_list(request):
    cat = Category.objects.all()
    prod = Product.objects.all().order_by('price')[:6]
    return render(request, 'mainapp/catalog.html',{'categories': cat, 'products': prod})


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/components/product.html'
    context_object_name = 'product'
    slug_field = 'name'

# def product_detail(request, slug):
#     update_price_from_file(slug)
#     obj = get_object_or_404(Product, name=slug)
#     # context = {'product': obj, 'new_price': obj.price * (1 - obj.discount / 100)}
#     return render(request, 'mainapp/components/product.html', {'product': obj})


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = reverse_lazy('products:catalog')
    slug_field = 'name'
    login_url = reverse_lazy('auth:login')


# def product_update(request, title):
#     success_url = reverse_lazy('catalog')
#     obj = get_object_or_404(Product, name=title)
#     form = ProductModelForm(instance=obj)
#     if request.method == 'POST':
#         form = ProductModelForm(
#             request.POST,
#             instance=obj
#         )
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     return render(request, 'create.html', {'form': form})

# Страницы товаров из каталога
# def mainapp_area_comfort(request):
#     update_database('Уголок')
#     table = Product.objects.get(name='Уголок')
#     context = {'product': table, 'new_price': table.price * (1 - table.discount / 100)}
#     return render(request, 'mainapp/products/area_comfort.html', context)
#
#
# def mainapp_kitchen_set(request):
#     update_database('Гарнитур')
#     table = Product.objects.get(name='Гарнитур')
#     context = {'product': table, 'new_price': table.price * (1 - table.discount / 100)}
#     return render(request, 'mainapp/products/kitchen_set.html', context)
#
#
# def mainapp_sofa(request):
#     update_database('Диван')
#     table = Product.objects.get(name='Диван')
#     context = {'product': table, 'new_price': table.price * (1 - table.discount / 100)}
#     return render(request, 'mainapp/products/sofa.html', context)
#
#
# def mainapp_table(request):
#     update_database('Стол')
#     table = Product.objects.get(name='Стол')
#     context = {'product': table, 'new_price': table.price * (1 - table.discount / 100)}
#
#     return render(request, 'mainapp/components/product.html', context)

# class ProductList(ListView):
#     model = Product
#     template_name = 'mainapp/catalog.html'
#     context_object_name = 'categories'
#     def get_context_data(self, **kwargs):
#         context = super(ProductList, self).get_context_data(**kwargs)
#         context['products'] = Product.objects.all()
#         return context

# def product_create(request):
#
#     success_url = reverse_lazy('products:catalog')
#     form = ProductModelForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             # return redirect('/')
#             return redirect(success_url)
#     return render(request, 'create.html', {'form': form})
#

#  def product_create(request):
#
#     form = forms.ProductForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             category = form.cleaned_data.get('category')
#             image = form.cleaned_data.get('image')
#             short_desc = form.cleaned_data.get('short_desc')
#             desc = form.cleaned_data.get('desc')
#             price = form.cleaned_data.get('price')
#             discount = form.cleaned_data.get('discount')
#             quantity = form.cleaned_data.get('quantity')
#
#        Product.objects.create(
#             name=name,
#             category=category,
#             image=image,
#             short_desc=short_desc,
#             desc=desc,
#             price=price,
#             discount=discount,
#             quantity=quantity
#              )
#
#     return render(request, 'create.html', {'form': form})