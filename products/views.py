from django.shortcuts import render
from .models import product
from django.core.paginator import Paginator
def index(request):
    featured_products=product.objects.order_by('-priority')[:4]
    latest_products=product.objects.order_by('-created_at')[:4]
    context={'featured_products':featured_products,'latest_products':latest_products}
    

    return render(request, 'index.html',context)
def product_list(request):
    
    product_list=product.objects.order_by('-priority').filter(delete_status=1)
    product_paginator=Paginator(product_list,10)
    product_list=product_paginator.get_page(request.GET.get('page'))
    context={'products':product_list}
    return render(request,'products.html',context)

def product_detail(request,pk):
    product_obj=product.objects.get(id=pk)
    context={'product':product_obj}
    return render(request,'product_detail.html',context)

