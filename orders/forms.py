from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput, NumberInput, inlineformset_factory, BaseInlineFormSet
from django.utils.datetime_safe import date

from northwind.models import Order, OrderDetail, Product


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'employee', 'order_date', 'required_date',
                  'ship_via', 'freight', 'ship_name', 'ship_address', 'ship_city',
                  'ship_region', 'ship_postal_code', 'ship_country']

        widgets = {
            'order_date': DateInput(attrs={"type": "date"}),
            'required_date': DateInput(attrs={"type": "date"}),
            'freight': NumberInput(attrs={"type": "number", "min": "0"}),
        }

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        for key in self.fields:
            self.fields[key].required = True

    def clean_order_date(self):
        d = self.cleaned_data.get("order_date")
        if d > date.today():
            raise ValidationError("Orders cannot be from future")
        return d

    def clean_required_date(self):
        d = self.cleaned_data.get("required_date")
        if d <= date.today():
            raise ValidationError("Required date cannot be from past")
        return d


class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['product', 'quantity', 'discount']

        widgets = {
            'quantity': NumberInput(attrs={"type": "number", "min": "1"}),
            'discount': NumberInput(attrs={"type": "number", "min": "0", "max": 100})
        }

    def __init__(self, *args, **kwargs):
        super(OrderDetailForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        for key in self.fields:
            self.fields[key].required = True
        self.fields['product'].queryset = Product.objects.filter(discontinued=0, units_in_stock__gt=0)


class BaseOrderDetailFormSet(BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            return
        products = []
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue
            product = form.cleaned_data.get('product')
            if product in products:
                raise ValidationError(f"Products must be different. The same product: {product.product_name}")
            products.append(product)

            quantity = form.cleaned_data.get('quantity')
            if quantity > product.units_in_stock:
                raise ValidationError(f"Not enough units in stock for {product.product_name}. In stock is unit: {product.units_in_stock}")


OrderDetailFormSet = inlineformset_factory(Order, OrderDetail, form=OrderDetailForm, formset=BaseOrderDetailFormSet,
                                           can_delete=False, extra=1)
