from django.shortcuts import render

def index(request):
    indices = [str(i) for i in range(5, 13)]
    return render(request, 'index.html', {'indices': indices})
def products(request):
    return render(request,'products.html')
def product_detail(request):
    return render(request,'product_detail.html')

