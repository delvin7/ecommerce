from django.shortcuts import render
from .models import product
from django.core.paginator import Paginator
def index(request):
    indices = [str(i) for i in range(5, 13)]
    return render(request, 'index.html', {'indices': indices})
def product_list(request):
   
    product_list=product.objects.all()
    product_paginator=Paginator(product_list,10)
    product_list=product_paginator.get_page(request.GET.get('page'))
    context={'products':product_list}
    return render(request,'products.html',context)
def product_detail(request):
    return render(request,'product_detail.html')

