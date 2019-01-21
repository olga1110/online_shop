import json
# import simplejson
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404, render_to_response
from django.template.loader import get_template
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.db import models
from django.views.generic import (
    TemplateView,
    FormView, CreateView, UpdateView,
    DeleteView, ListView, DetailView,
)
from django.views.generic.list import MultipleObjectMixin
from django.forms.models import modelformset_factory

from mainapp.models import Category, Product
from mainapp.forms import CategoryForm, CategoryModelForm
from django.contrib.auth.decorators import user_passes_test
from mainapp.mixins import SuperUserMixin

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

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
        context['OK_text'] = 'Добавить'
        return context


CategoryFormset = modelformset_factory(Category, form=CategoryModelForm,
                                       max_num=10, validate_max=True,
                                       help_texts={'name': 'Название категории должно быть уникальным'}, can_order=True,
                                       can_delete=True)


class CategoryFormSet(TemplateView):
    template_name = 'category_formset.html'
    formset = None

    def get(self, request, *args, **kwargs):
        self.formset = CategoryFormset()
        return super(CategoryFormSet, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryFormSet, self).get_context_data(**kwargs)
        context['formset'] = self.formset
        context['title'] = 'Набор форм для Категории товара'
        return context

    def post(self, request, *args, **kwargs):
        self.formset = CategoryFormset(request.POST)
        if self.formset.is_valid():
            self.formset.save()
            return redirect('products:catalog')
        return super(CategoryFormSet, self).post(request, *args, **kwargs)


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

def search_products(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    if search_text != '':
        products = Product.objects.filter(short_desc__contains=search_text)
    return render_to_response('mainapp/components/ajax_search.html', {'objects': products,
                                                                      'search_url': 'categories:search_products'})