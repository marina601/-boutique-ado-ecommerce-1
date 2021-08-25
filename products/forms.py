from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Creating a form to add products to the database
    """

    class Meta:
        model = Product
        fields = '__all__'  # all will include all the fields
    
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Get all the category model fields and display them by friendly name
        no id
        """
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            """ Add classes to the form fields"""
            field.widget.attrs['class'] = 'border-black rounded-0'
