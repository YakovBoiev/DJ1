from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    def create_links_menu():
        links_menu = []
        spam_dict = {'href': 'products_all', 'name': 'все'}
        links_menu.append(spam_dict)
        categories = ProductCategory.objects.all()
        for category in categories:
            spam_dict = {}
            spam_dict['href'] = f'product_category_{category.id}'
            spam_dict['name'] = category.name
            links_menu.append(spam_dict)
        return links_menu

    title = 'Каталог'
    links_menu = create_links_menu()
    products = Product.objects.all()[:3]

    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': products
    }
    return render(request, 'mainapp/products.html', context)
