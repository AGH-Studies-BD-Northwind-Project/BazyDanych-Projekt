from django.shortcuts import render
from django.views import generic

from northwind.models import Order


def orders(request):
    return render(request, 'orders/order_list.html',
                  {"orders": Order.objects.all().order_by('order_id')})

class DetailView(generic.DetailView):
    model = Order
    template_name = 'orders/order_detail.html'

    def totalPrice(self):
        total = 0
        for i in self.get_object().orderdetail_set.values():
            total += (1 - i.get('discount')) * i.get('quantity') * i.get('unit_price')
        return total + self.get_object().freight

def upload(request):
    return render(request, "orders/order_add.html")





