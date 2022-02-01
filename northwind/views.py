from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreate
from django.http import HttpResponse

def index(request):
    products = Product.objects.all()
    return render(request, 'northwind/product_list.html', {'products': products})

def upload(request):
    upload = ProductCreate()
    if request.method == 'POST':
        upload = Product(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'northwind/product_upload_form.html', {'upload_form': upload})

def update_product(request, product_id):
    product_id = int(product_id)
    try:
        product = Product.objects.get(product_id)
    except Product.DoesNotExist:
        return redirect('index')
    product_form = ProductCreate(request.POST or None, instance=product)
    if product_form.is_valid():
       product_form.save()
       return redirect('index')
    return render(request, 'northwind/product_upload_form.html', {'upload_form':product_form})

def delete_product(request, product_id):
    product_id = int(product_id)
    try:
        product = Product.objects.get(product_id)
    except Product.DoesNotExist:
        return redirect('index')
    product.delete()
    return redirect('index')


