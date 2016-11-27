from django import forms
from django.forms import BaseFormSet

from .models import Recipe
from .models import Step
from .models import QuantityType
from .models import Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        # exclude = ['publish']


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        exclude = ['rid']


class QuantityTypeForm(forms.ModelForm):
    class Meta:
        model = QuantityType
        fields = '__all__'


class IngredientForm(forms.ModelForm):
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


class ImageUploadForm(forms.Form):
    imagefile = forms.FileField(
        label='Select a file'
    )
