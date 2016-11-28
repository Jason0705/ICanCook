from django import forms
from django.forms import BaseFormSet, TextInput, Textarea

from .models import Recipe
from .models import Step
from .models import QuantityType
from .models import Ingredient


class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'class': 'form-control', 'placeholder': 'Title'}
        self.fields['description'].widget.attrs = {'class': 'form-control', 'placeholder': 'Description'}
        self.fields['prep_time'].widget.attrs = {'class': 'form-control', 'placeholder': 'Prep Time'}

    class Meta:
        model = Recipe
        exclude = ('userid',)
        fields = '__all__'
        # exclude = ['publish']


class StepForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StepForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs = {'class': 'form-control', 'placeholder': 'Description', 'rows': '5'}
        self.fields['order'].widget.attrs = {'class': 'form-control', 'placeholder': 'Order'}

    class Meta:
        model = Step
        widgets = {
            'description': Textarea(),
        }
        exclude = ('rid',)
        fields = '__all__'


class QuantityTypeForm(forms.ModelForm):
    class Meta:
        model = QuantityType
        fields = '__all__'


class IngredientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control', 'placeholder': 'Name'}
        self.fields['quantity'].widget.attrs = {'class': 'form-control', 'placeholder': 'Quantity'}
        self.fields['quantity_type'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Ingredient
        exclude = ('rid',)
        fields = '__all__'


class BaseIngredientFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return

        for form in self.forms:
            if form.cleaned_data:
                ingr_name = form.cleaned_data['name']
                ingr_quantity = form.cleaned_data['quantity']
                ingr_quantity_type = form.cleaned_data['quantity_type']

                field_count = 0

                if ingr_name:
                    field_count += 1

                if ingr_quantity:
                    field_count += 1

                if ingr_quantity_type:
                    field_count += 1

                if 0 < field_count < 3:
                    raise forms.ValidationError('Please fill in all fields.')


class BaseStepsFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return


# class ImageUploadForm(forms.Form):
#     imagefile = forms.FileField(
#         label='Select a file'
#     )
