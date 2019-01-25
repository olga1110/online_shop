from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (
    FormView, CreateView, UpdateView,
    DeleteView, ListView, DetailView,
)
from django.contrib import messages

from . import forms
from basketapp.models import Basket
from mainapp.models import Product


# @login_required
# def basket(request):
#     basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
#     return render(request, 'basketapp/basket.html', {'basket_items': basket_items})

class BasketList(LoginRequiredMixin, ListView):
    model = Basket
    template_name = 'basketapp/basket.html'
    context_object_name = 'basket_items'

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user).order_by('product__category')
        return queryset


@login_required
def basket_add(request, pk):
    product = get_object_or_404(Product, id=pk)
    form = forms.CartForm(request.POST)
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product_detail', args=[product.name]))

    if form.is_valid():
        if form.cleaned_data.get('quantity'):
            quantity = int(form.cleaned_data.get('quantity'))
        else:
            quantity = 1
        # Проверка остатков на складе
        if product.quantity == 0:
            messages.add_message(request, messages.INFO, f'К сожалению, на данный момент товар отсутствует на складе')
        else:
            if quantity > product.quantity:
                messages.add_message(request, messages.INFO,
                                     f'На данный момент возможен заказ только {product.quantity}'
                                     f' единиц(-ы) товара!')
                quantity = product.quantity

            old_basket_item = Basket.objects.filter(user=request.user, product=product)
            if old_basket_item:
                old_basket_item[0].quantity += int(quantity)
                old_basket_item[0].save()
            else:
                new_basket_item = Basket(user=request.user, product=product)
                new_basket_item.quantity += int(quantity)
                new_basket_item.save()
            product.quantity = product.quantity - quantity
            product.save()
            messages.add_message(request, messages.INFO, 'Товар добавлен в корзину')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def order_send(request):
    return render(request, 'basketapp/order_form.html', {})


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove_all(request):
    Basket.objects.filter(user=request.user).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
