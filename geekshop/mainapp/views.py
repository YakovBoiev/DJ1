import random

from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_hot_product():
    product = Product.objects.all()
    return random.sample(list(product), 1)[0]

def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products



def index(request, pk=None, page=1):

    title = 'Продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все', 'pk': 0}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk)

        paginator = Paginator(products, 3)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
        }

        return render(request, 'mainapp/products_list.html', context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'Продукты'
    links_menu = ProductCategory.objects.all()
    product = get_object_or_404(Product, pk=pk)
    same_products = get_same_products(product)

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product,
        'same_products': same_products,
    }
    return render(request, 'mainapp/product.html', context)
