import random

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    title = 'Корзина'
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')

    context = {
        'title': title,
        'basket_items': basket_items,
    }
    return render(request, 'basketapp/basket.html', context)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
