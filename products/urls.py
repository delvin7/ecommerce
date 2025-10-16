# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.product_list, name='products_list'),
    path('product_detail/', views.product_detail, name='product_detail'),

]