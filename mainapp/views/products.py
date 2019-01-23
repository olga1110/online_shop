import json

from django.contrib.auth.decorators import user_passes_test
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    FormView, CreateView, UpdateView,
    DetailView,
)

from mainapp.forms import ProductModelForm
from basketapp.forms import CartForm
from mainapp.mixins import SuperUserMixin
from mainapp.models import Product, Category


def update_price_from_file(product):
    obj = Product.objects.get(name=product)
    path = 'mainapp/static/mainapp/files/description.json'
    with open(path) as json_data:
        data = json.load(json_data)

    obj.price = data['description'][product]
    obj.save()


def mainapp_Contacts(request):
    path = 'mainapp/static/mainapp/files/organization.json'
    with open(path, encoding='utf-8') as json_data:
        context = json.load(json_data)

    # template = get_template('mainapp/Сontacts.html')
    # return HttpResponse(template.render(context))

    return render(request, 'mainapp/contacts.html', context)


def mainapp_index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'company':
                   {'title': 'cozy kitchen',
                    'advertisement': 'Самая лучшая мебель для кухни здесь!!!'},
               'products': products,
               'categories': categories,
               }
    return render(request, 'mainapp/index.html', context)


# def mainapp_registration(request):
#     context = {'reg': 'Регистрация'}
#     return render(request, 'mainapp/registration.html', context)

# CRUD-методы


class ProductGenericCreate(SuccessMessageMixin, SuperUserMixin, CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'create.html'
    success_url = reverse_lazy('products:catalog')
    success_message = 'Товар успешно добавлен в список'

    def get_context_data(self, **kwargs):
        context = super(ProductGenericCreate, self).get_context_data(**kwargs)
        context['url_cancel'] = 'products:catalog'
        context['title'] = 'Добавление товара'
        context['OK_text'] = 'Добавить'
        return context


class ProductGenericUpdate(SuperUserMixin, UpdateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'create.html'
    # success_url = reverse_lazy('products:catalog')
    slug_field = 'name'

    def get_context_data(self, **kwargs):
        context = super(ProductGenericUpdate, self).get_context_data(**kwargs)
        context['url_cancel'] = 'categories:category'
        context['category_product'] = self.object.category.name
        context['OK_text'] = 'Сохранить'
        return context

    def get_success_url(self):
        return reverse('categories:category', kwargs={'slug': self.object.category.name})


class ProductCreate(SuperUserMixin, View):
    template_name = 'create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('products:catalog')

    def get(self, request):
        form = ProductModelForm()
        return render(request, self.template_name, {self.context_object_name: form})

    def post(self, request):
        form = ProductModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {self.context_object_name: form})


class ProductUpdate(SuperUserMixin, FormView):
    form_class = ProductModelForm
    success_url = reverse_lazy('products:catalog')
    template_name = 'create.html'
    slug_field = 'name'

    def post(self, request, title):
        obj = get_object_or_404(Product, name=title)
        form = self.form_class(
            request.POST,
            instance=obj
        )
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


def category_product_list(request, page=1):
    cat = Category.objects.filter(is_active=1)
    prod = Product.objects.filter(is_active=1, category__is_active=1).order_by('category', 'price')
    paginator = Paginator(prod, 4)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    return render(request, 'mainapp/catalog.html', {'categories': cat, 'products': products_paginator})


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/product.html'
    context_object_name = 'product'
    slug_field = 'name'


    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        form = CartForm(self.request.POST)
        queryset = Product.objects.all()
        product = queryset.get(name=self.kwargs['slug'])
        category = product.category.name
        context['url_cancel'] = '/catalog/' + category
        context['form'] = form
        return context

    # def get_object(self):
    #     queryset = Product.objects.all()
    #     product = queryset.get(name=self.kwargs['slug']).category.name
    #     category = product.category.name
    #
    #     return queryset.get(name=self.kwargs['slug'])

# def product_detail(request, slug):
#     update_price_from_file(slug)
#     obj = get_object_or_404(Product, name=slug)
#     # context = {'product': obj, 'new_price': obj.price * (1 - obj.discount / 100)}
#     return render(request, 'mainapp/product.html', {'product': obj})


# class ProductDelete(SuperUserMixin, DeleteView):
#     model = Product
#     template_name = 'delete.html'
#     # success_url = reverse_lazy('products:catalog')
#     slug_field = 'name'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductDelete, self).get_context_data(**kwargs)
#         context['url_cancel'] = 'categories:category'
#         context['category_product'] = self.object.category.name
#         return context
#
#     def get_success_url(self):
#         return reverse('categories:category', kwargs={'slug': self.object.category.name})


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, slug):

    product = get_object_or_404(Product, name=slug)
    content = {'object_to_delete': product, 'title': 'Удаление продукта', 'subject': 'продукта',
               'name': product.name, 'part_name': 'Архив', 'url_cancel': request.META.get('HTTP_REFERER', '/')}
    print(request.META.get('HTTP_REFERER', '/'))
    if request.method == 'POST':
        product.is_active = False
        product.save()
        # return HttpResponseRedirect(reverse('products:catalog'))
        return reverse('categories:category', kwargs={'slug': product.category.name})
    return render(request, 'delete.html', content)


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
#     return render(request, 'mainapp/product.html', context)

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

def search_categories(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        categories = Category.objects.filter(short_desc__contains=search_text)
    else:
        search_text = ''
        categories = {}
    return render_to_response('mainapp/components/ajax_search.html', {'objects': categories})
