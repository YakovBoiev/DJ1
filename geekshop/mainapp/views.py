from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product


def index(request, pk=None):

    title = 'Продукты'
    links_menu = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk)

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products
        }

        return render(request, 'mainapp/products_list.html', context)

    products = Product.objects.all()[:3]

    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': products
    }
    return render(request, 'mainapp/products.html', context)
