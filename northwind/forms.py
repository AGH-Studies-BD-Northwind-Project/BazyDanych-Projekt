from django import forms
from django.forms import modelform_factory, NumberInput

from .models import Product

class ProductCreate(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'unit_price': NumberInput(attrs={"type": "number", "min":"0"}),
            'units_in_stock': NumberInput(attrs={"type": "number", "min": "0"}),
            'units_on_order': NumberInput(attrs={"type": "number", "min": "0"}),
            'reorder_level': NumberInput(attrs={"type": "number", "min": "0"}),
            'discontinued': NumberInput(attrs={"type": "number", "min": "0", "max":1})
        }
    def clean_discontinued(self):
        d = self.cleaned_data.get("discontinued")
        if d != 0 and d != 1:
            raise ValueError("Only accepted values are 0 or 1")
        return d