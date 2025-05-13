from django import forms

from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class':'form-control w-25',
                    'placeholder': 'Ingrese el nombre del producto',
                    'style':'background: aquamarine'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class':'form-control w-25',
                    'placeholder': 'Ingrese el valor del precio',
                    'style':'background: orange'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class':'form-control w-25',
                    'placeholder': 'Ingrese el valor del stock',
                    'style':'background: yellow'
                }
            ),
        }