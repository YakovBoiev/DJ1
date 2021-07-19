from django.shortcuts import render


def index(request):
    title = 'Каталог'
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'product_home', 'name': 'дом'},
        {'href': 'product_office', 'name': 'офис'},
        {'href': 'product_modern', 'name': 'модерн'},
        {'href': 'product_classic', 'name': 'классика'},

    ]
    context = {
        'title': title,
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)
