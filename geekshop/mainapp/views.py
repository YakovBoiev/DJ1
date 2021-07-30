from django.shortcuts import render
from .models import ProductCategory, Product


def index(request, pk=None):

    title = 'Продукты'
    links_menu = ProductCategory.objects.all()




    products = Product.objects.all()[:3]

    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': products
    }
    return render(request, 'mainapp/products.html', context)
