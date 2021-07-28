from django.shortcuts import render


def login(request):
    title = 'Вход'
    context = {
        'title': title
    }
    return render(request, 'authapp/base.html', context)


def logout(request):
    pass
