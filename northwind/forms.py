from django import forms
from django.core.exceptions import ValidationError
from django.forms import NumberInput

from .models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'supplier', 'category', 'quantity_per_unit', 'unit_price',
                  'units_in_stock', 'units_on_order', 'reorder_level', 'discontinued', 'picture']
        widgets = {
            'unit_price': NumberInput(attrs={"type": "number", "min": "0"}),
            'units_in_stock': NumberInput(attrs={"type": "number", "min": "0"}),
            'units_on_order': NumberInput(attrs={"type": "number", "min": "0"}),
            'reorder_level': NumberInput(attrs={"type": "number", "min": "0"}),
            'discontinued': NumberInput(attrs={"type": "number", "min": "0", "max": 1})
        }

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_discontinued(self):
        d = self.cleaned_data.get("discontinued")
        if d != 0 and d != 1:
            raise ValidationError("Only accepted values are 0 or 1")
        return d


class SubmitSearchForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(SubmitSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    name = forms.CharField(label='Search', required=False)
