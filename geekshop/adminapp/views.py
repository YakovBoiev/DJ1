from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from django.contrib.auth.decorators import user_passes_test

from .forms import ProductCategoryEditForm, ProductEditForm
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#     user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': title,
#         'user_list': user_list,
#     }
#
#     return render(request, 'adminapp/users.html', context)

class UserListView(ListView, LoginRequiredMixin):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data()
        title = 'админка/пользователи'
        context['title'] = title
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'пользователи/создание'
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     context = {
#         'title': title,
#         'update_form': user_form,
#     }
#
#     return render(request, 'adminapp/user_update.html', context)

class UserCreateView(CreateView, LoginRequiredMixin):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    form_class = ShopUserRegisterForm
    success_url = reverse_lazy('admin_staff:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data()
        title = 'пользователи/создание'
        context['title'] = title
        return context



@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактирование'
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = ShopUserEditForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_staff:users'))
    else:
        user_form = ShopUserEditForm(instance=user)

    context = {
        'title': title,
        'update_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:users'))


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'админка/категории'
    categories_list = ProductCategory.objects.all()
    context = {
        'title': title,
        'categories_list': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'Категории/создание'
    if request.method == 'POST':
        update_form = ProductCategoryEditForm(request.POST, request.FILES,)
        update_form.save()
        return HttpResponseRedirect(reverse('admin_staff:categories'))
    else:
        update_form = ProductCategoryEditForm()

    context = {
        'title': title,
        'update_form': update_form,
    }
    return render(request, 'adminapp/categories_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'Категории/редактирование'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        update_form = ProductCategoryEditForm(request.POST, request.FILES, instance=category)
        update_form.save()
        return HttpResponseRedirect(reverse('admin_staff:categories'))
    else:
        update_form = ProductCategoryEditForm(instance=category)

    context = {
        'title': title,
        'update_form': update_form,
    }
    return render(request, 'adminapp/categories_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    category.delete()
    return HttpResponseRedirect(reverse('admin_staff:categories'))


@user_passes_test(lambda u: u.is_superuser)
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


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'продукты/создание'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES,)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('adminapp:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})

    context = {
        'title': title,
        'update_form': product_form,
        'category': category
    }

    return render(request, 'adminapp/product_update.html', context)

# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#      title = 'продукты/подробнее'
#      product = get_object_or_404(Product, pk=pk)
#
#      context = {
#          'title': title,
#          'product': product,
#      }
#
#      return render(request, 'adminapp/product_read.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        title = 'продукты/подробнее'
        context['title'] = title
        return context



@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'продукты/редактироание'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('adminapp:products', args=[product.category.pk]))
    else:
        product_form = ProductEditForm(instance=product)

    context = {
        'title': title,
        'update_form': product_form,
        'category': product.category
    }

    return render(request, 'adminapp/product_update.html', context)


def product_delete(request, pk):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=pk)
        if product.is_active == True:
            product.is_active = False
        else:
            product.is_active = True
        product.save()
        return HttpResponseRedirect(reverse('adminapp:products', args=[product.category.pk]))











