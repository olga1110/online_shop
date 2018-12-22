from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from basketapp.models import Basket
from mainapp.models import Product
from django.views.generic import (
    FormView, CreateView, UpdateView,
    DeleteView, ListView, DetailView,
    )


# @login_required
# def basket(request):
#     basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
#     return render(request, 'basketapp/basket.html', {'basket_items': basket_items})


class BasketList(LoginRequiredMixin, ListView):
    model = Basket
    template_name = 'basketapp/basket.html'
    context_object_name = 'basket_items'

    def get_context_data(self, **kwargs):
        context = super(BasketList, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user).order_by('product__category')
        return queryset


@login_required
def basket_add(request, pk):
    product_name = get_object_or_404(Product, id=pk)

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product_detail', args=[product_name.name]))
    product = get_object_or_404(Product, pk=pk)
    old_basket_item = Basket.objects.filter(user=request.user, product=product)
    if old_basket_item:
        old_basket_item[0].quantity += 1
        old_basket_item[0].save()
    else:
        new_basket_item = Basket(user=request.user, product=product)
        new_basket_item.quantity += 1
        new_basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return HttpResponseRedirect('basketapp/basket.html')



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

