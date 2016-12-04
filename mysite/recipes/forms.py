from django import forms
from django.forms import BaseFormSet, TextInput, Textarea

from .models import Recipe
from .models import Step
from .models import QuantityType
from .models import Ingredient
from .models import Category


class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'class': 'form-control', 'placeholder': 'Title'}
        self.fields['description'].widget.attrs = {'class': 'form-control', 'placeholder': 'Description'}
        self.fields['prep_time'].widget.attrs = {'class': 'form-control', 'placeholder': 'Prep Time'}
        self.fields['calorie'].widget.attrs = {'class': 'form-control', 'placeholder': 'Calorie'}
        self.fields['serving'].widget.attrs = {'class': 'form-control', 'placeholder': 'Serving'}

    class Meta:
        model = Recipe
        exclude = ('userid', 'favourites', 'updated')
        fields = '__all__'
        # exclude = ['publish']


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['breakfast'].widget.attrs = {'class': 'form-check-input'}
        self.fields['lunch'].widget.attrs = {'class': 'form-check-input'}
        self.fields['dinner'].widget.attrs = {'class': 'form-check-input'}
        self.fields['dessert'].widget.attrs = {'class': 'form-check-input'}
        self.fields['holiday'].widget.attrs = {'class': 'form-check-input'}

    class Meta:
        model = Category
        exclude = ('rid',)
        fields = '__all__'


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
        self.fields['quantity'].widget.attrs = {'class': 'form-control', 'placeholder': 'Quantity', 'step': '0.25'}
        self.fields['quantity_type'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Ingredient
        exclude = ('rid',)
        fields = '__all__'


class BaseIngredientFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return

        validcount = 0

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

                validcount += 1

        if validcount == 0:
            raise forms.ValidationError('At least one ingredient required.')


class BaseStepsFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return

        validforms = 0

        for form in self.forms:
            if len(form.cleaned_data) > 0:
                validforms += 1

        if validforms == 0:
            raise forms.ValidationError('At least one step required.')

# class ImageUploadForm(forms.Form):
#     imagefile = forms.FileField(
#         label='Select a file'
#     )
