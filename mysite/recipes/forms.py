from django import forms

from .models import Recipe
from .models import Step
from .models import QuantityType
from .models import Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


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
