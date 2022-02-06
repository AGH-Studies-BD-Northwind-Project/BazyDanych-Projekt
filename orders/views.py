from django.shortcuts import render, get_object_or_404

from northwind.models import Order


def orders(request):
    return render(request, 'orders/order_list.html',
                  {"orders": Order.objects.all().order_by('order_id')})

def detail(request, id):
    order = get_object_or_404(Order, pk=id)
    return render(request, "orders/order_detail.html", {"order": order})

def upload(request):
    return render(request, "orders/order_add.html")


