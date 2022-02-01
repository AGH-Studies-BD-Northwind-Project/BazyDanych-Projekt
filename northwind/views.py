from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductCreate
from django.http import HttpResponse

def products(request):
    products = Product.objects.all()
    return render(request, 'northwind/product_list.html', {'products': products})

def deatil_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "northwind/product_detail.html", {"product": product})

def upload_product(request):
    if request.method == 'POST':
        upload = ProductCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('products')
    else:
        upload = ProductCreate()
    return render(request, 'northwind/product_upload_form.html', {'upload_form': upload})

def update_product(request, id):
    product_id = id
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return redirect('products')
    product_form = ProductCreate(request.POST or None, instance=product)
    if product_form.is_valid():
       product_form.save()
       return redirect('products')
    return render(request, 'northwind/product_upload_form.html', {'upload_form':product_form})

def delete_product(request, id):
    product_id = id
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return redirect('products')
    product.delete()
    return redirect('products')






