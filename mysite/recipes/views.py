from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse

from .models import Recipe, Step, QuantityType, Ingredient
from .forms import RecipeForm, StepForm, QuantityTypeForm, IngredientForm


# Create your views here.

def index(request):
    recipe_names = Recipe.objects.order_by('-title')
    context = {'recipe_names': recipe_names}

    return render(request, 'recipes/index.html', context)


def details(request, rid):
    try:
        recipe = Recipe.objects.get(pk=rid)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist.")
    return render(request, 'recipes/details.html', {'recipe': recipe})


def add_recipe(request):
    Recipe_Form = RecipeForm(request.POST or None)
    Step_Form = StepForm(request.POST or None)
    QuantityType_Form = QuantityTypeForm(request.POST or None)
    Ingredient_Form = IngredientForm(request.POST or None)

    if Recipe_Form.is_valid():
        new_recipe = Recipe_Form.save(commit=False)
        new_recipe.save()

    if Step_Form.is_valid():
        new_step = Step_Form.save(commit=False)
        new_step.save()

    if QuantityType_Form.is_valid():
        new_QuantityType = QuantityType_Form.save(commit=False)
        new_QuantityType.save()

    if Ingredient_Form.is_valid():
        new_ingredient = IngredientForm.save(commit=False)
        new_ingredient.save()

    recipe_names = Recipe.objects.order_by('-rid')[:5]
    context = {'Recipe_Form': Recipe_Form, 'Step_Form': Step_Form, 'QuantityType_Form': QuantityType_Form, 'Ingredient_Form': Ingredient_Form,
               'recipe_names': recipe_names}

    return render(request, 'recipes/add.html', context)


def edit(request, rid):
    edit_recipe = Recipe.objects.get(pk=rid)
    if request.POST:
        recipe_form = RecipeForm(request.POST, instance=edit_recipe)
        context = {'recipe_form': recipe_form}
        if recipe_form.is_valid():
            recipe_form.save()
    else:
        recipe_form = RecipeForm(instance=edit_recipe)
        context = {'recipe_form': recipe_form}
    return render(request, 'recipes/edit.html', context)


def delete(request, rid):
    delete = Recipe.objects.filter(pk=rid).delete()
    return render(request, 'recipes/delete.html')
