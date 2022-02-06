from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput, NumberInput
from django.utils.datetime_safe import date

from northwind.models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'employee', 'order_date',
                  'ship_via', 'freight','ship_name', 'ship_address', 'ship_city',
                  'ship_region', 'ship_postal_code', 'ship_country' ]
        widgets = {
            'order_date': DateInput(attrs={"type": "date"}),
            'freight': NumberInput(attrs={"type": "number", "min": "0"}),
        }

    def clean_order_date(self):
        d = self.cleaned_data.get("order_date")
        if d > date.today():
            raise ValidationError("Orders cannot be from future")
        return d

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        for key in self.fields:
            self.fields[key].required = True




