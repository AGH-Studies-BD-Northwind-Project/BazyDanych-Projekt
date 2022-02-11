from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView

from northwind.models import Order
from orders.forms import OrderCreateForm, OrderDetailFormSet


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


class OrderAddView(TemplateView):
    template_name = "orders/order_upload.html"

    def get(self, *args, **kwargs):
        order = Order()
        form_order = OrderCreateForm(instance=order)
        formset_prod = OrderDetailFormSet(instance=order)
        return self.render_to_response({'prod_formset': formset_prod, 'order_form': form_order})

    def post(self, *args, **kwargs):
        order = Order()
        form_order = OrderCreateForm(data=self.request.POST)
        formset_prod = OrderDetailFormSet(data=self.request.POST, instance=order)
        if form_order.is_valid() and formset_prod.is_valid():
            a = form_order.save(commit=False)
            a.save()
            prods = formset_prod.save(commit=False)
            for prod in prods:
                prod.order_id = a.order_id
                prod.unit_price = prod.product.unit_price
                prod.discount /= 100
                prod.save()
                prod.product.units_in_stock -= prod.quantity
                prod.product.save()

            return redirect('orders')

        return self.render_to_response({'prod_formset': formset_prod, 'order_form': form_order})
