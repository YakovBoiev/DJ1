from django.urls import path
from .views import index, product

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='products_all'),
    path('category/<int:pk>', index, name='category'),
    path('product/<int:pk>', product, name='product' )
]
