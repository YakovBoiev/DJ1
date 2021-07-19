from django.shortcuts import render


def index(request):
    title = 'магазин'
    context = {
        'title': title,
        'slogan': 'супер предложение',
        }

    return render(request, 'geekshop/index.html', context)

def contacts(request):
    title = 'kонтакты'
    context = {
        'title': title
    }

    return render(request, 'geekshop/contact.html', context)
