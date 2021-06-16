from django import forms
from .models import Product
from crispy_forms.helper import FormHelper


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {'title', 'slug', 'category', 'description',
                  'price', 'image', 'stock', 'is_active'}

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    