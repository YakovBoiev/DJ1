from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


def users(request):
    title = 'админка/пользователи'
    user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'user_list': user_list,
    }

    return render(request, 'adminapp/users.html', context)

def user_create(request):
    title = 'пользователи/создание'
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_staff:users'))
    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'update_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', context)


def categories(request):
    title = 'админка/категории'
    categories_list = ProductCategory.objects.all()
    context = {
        'title': title,
        'categories_list': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


def category_update():
    pass


def category_delete():
    pass


def category_create():
    pass



def products(request, pk):
    title = 'админка/проодукты'
    category = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'product_list': product_list,
        'category': category,
    }

    return render(request, 'adminapp/products.html', context)






