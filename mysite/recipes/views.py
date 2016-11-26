from django.forms import formset_factory
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse

from .models import Recipe, Step, QuantityType, Ingredient
from .forms import RecipeForm, StepForm, QuantityTypeForm, IngredientForm, ImageUploadForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory



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


@login_required(login_url='/login/')
def add_recipe(request):
    recipe_form = RecipeForm()
    ingredients_formset_factory = formset_factory(IngredientForm)
    steps_formset_factory = formset_factory(StepForm)

    if request.POST:
        recipe_form = RecipeForm(request.POST)
        ingredients_form_set = ingredients_formset_factory(request.POST)
        step_form_set = steps_formset_factory(request.POST)

        if recipe_form.is_valid() and ingredients_form_set.is_valid() and step_form_set.is_valid() and image_form.is_valid():
	    recipe = recipe_form.save()

            for ingr_form in ingredients_form_set.forms:
                ingredient = ingr_form.save(commit=False)
                ingredient.rid_id = recipe.rid
                ingredient.save()

            for stp_form in step_form_set.forms:
                step = stp_form.save(commit=False)
                step.rid_id = recipe.rid
                step.save()

            recipe.save()
            return HttpResponseRedirect('/recipes/' + str(recipe.rid))

    context = {'Recipe_Form': recipe_form, 'Ingredient_Forms': ingredients_formset_factory, 'Step_Forms': steps_formset_factory}
    return render(request, 'recipes/add.html', context)


@login_required(login_url='/login/')
def edit(request, rid):
    edit_recipe = Recipe.objects.get(pk=rid)
    IngredientFormSet = modelformset_factory(Ingredient, form=IngredientForm)
    formset=IngredientFormSet(queryset=Ingredient.objects.filter(rid=rid))

    if request.POST:
        recipe_form = RecipeForm(request.POST, instance=edit_recipe)
        context = {'recipe_form': recipe_form,}
        if recipe_form.is_valid():
            recipe_form.save()
            return HttpResponseRedirect('/recipes/' + str(rid))
    else:
        recipe_form = RecipeForm(instance=edit_recipe)
        context = {'recipe_form': recipe_form, 'rid':rid, 'formset': formset}
    return render(request, 'recipes/edit.html', context)


@login_required(login_url='/login/')
def delete(request, rid):
    delete = Recipe.objects.filter(pk=rid).delete()
    return render(request, 'recipes/delete.html')
