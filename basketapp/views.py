from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from basketapp.models import Basket
from mainapp.models import Product


@login_required
def basket(request):
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
    return render(request, 'basketapp/basket.html', {'basket_items': basket_items})


@login_required
def basket_add(request, pk):
    product_name = get_object_or_404(Product, id=pk)
    # product_url = 'catalog/' + str(category_name) + '/' + str(product_name.name) + '/'

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
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



