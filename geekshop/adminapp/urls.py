from django.urls import path
from .views import users, user_create, categories, products, category_delete, category_update, category_create

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', user_create, name='user_create'),
    path('users/read/', users, name='users'),
    # path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    # path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    #
    path('categories/create/', category_create, name='category_create'),
    path('categories/read/', categories, name='categories'),
    path('categories/update/<int:pk>/', category_update, name='category_update'),
    path('categories/delete/<int:pk>/', category_delete, name='category_delete'),
    #
    # path('products/create/category/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', products, name='products'),
    # path('products/read/<int:pk>/', adminapp.product_read, name='product_read'),
    # path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    # path('products/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),

]
