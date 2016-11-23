from django.forms import formset_factory
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
    recipe_form = RecipeForm()
    ingredients_formset_factory = formset_factory(IngredientForm, extra=2)

    if request.POST:
        recipe_form = RecipeForm(request.POST)
        ingredients_form_set = ingredients_formset_factory(request.POST)

        if recipe_form.is_valid() and ingredients_form_set.is_valid():
            recipe = recipe_form.save()

            for ingr_form in ingredients_form_set.forms:
                ingredient = ingr_form.save(commit=False)
                ingredient.rid_id = recipe.rid
                ingredient.save()

            recipe.save()
            return HttpResponseRedirect('/recipe/' + str(recipe.rid))

    context = {'Recipe_Form': recipe_form, 'Ingredient_Forms': ingredients_formset_factory}
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
