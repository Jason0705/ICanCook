from urllib import quote_plus

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import formset_factory
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from .forms import RecipeForm, StepForm, IngredientForm, BaseIngredientFormSet, BaseStepsFormSet
from .models import Recipe


def index(request):
    recipe_names_list = Recipe.objects.all()  # .order_by('-created')

    paginator = Paginator(recipe_names_list, 10)  # Show 10 contacts per page

    page = request.GET.get('page')
    try:
        recipe_names = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        recipe_names = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        recipe_names = paginator.page(paginator.num_pages)

    context = {'recipe_names': recipe_names}

    return render(request, 'recipes/index.html', context)


def details(request, rid):
    try:
        recipe = Recipe.objects.get(pk=rid)
        share_string = quote_plus(recipe.description)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist.")

    context = {
        'recipe': recipe,
        'share_string': share_string
    }
    return render(request, 'recipes/details.html', context)


@login_required(login_url='/login/')
def add_recipe(request):
    StepFormSet = formset_factory(StepForm, formset=BaseStepsFormSet)
    IngredientFormSet = formset_factory(IngredientForm, formset=BaseIngredientFormSet)

    if request.POST:
        recipe_form = RecipeForm(request.POST)

        ingredient_formset = IngredientFormSet(request.POST, prefix='ingr')
        steps_formset = StepFormSet(request.POST, prefix='steps')

        if recipe_form.is_valid() and ingredient_formset.is_valid() and steps_formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.userid = request.user.id
            recipe.created = datetime.now()
            recipe.save()

            for ingr_form in ingredient_formset.forms:
                if ingr_form.is_valid() and ingr_form.has_changed():
                    ingr = ingr_form.save(commit=False)
                    ingr.rid_id = recipe.rid
                    ingr.save()

            for steps_form in steps_formset.forms:
                if steps_form.is_valid() and steps_form.has_changed():
                    step = steps_form.save(commit=False)
                    step.rid_id = recipe.rid
                    step.save()

            return HttpResponseRedirect('/recipes/' + str(recipe.rid))

    recipe_form = RecipeForm()
    ingredients_formset = IngredientFormSet(prefix='ingr')
    steps_formset = StepFormSet(prefix='steps')

    context = {'recipe_form': recipe_form, 'ingredients_formset': ingredients_formset, 'steps_formset': steps_formset}
    return render(request, 'recipes/add.html', context)


@login_required(login_url='/login/')
def edit(request, rid):
    edit_recipe = Recipe.objects.get(pk=rid)

    StepFormSet = formset_factory(StepForm, formset=BaseStepsFormSet)
    IngredientFormSet = formset_factory(IngredientForm, formset=BaseIngredientFormSet)

    ingredients = edit_recipe.ingredient_set.all()
    ingredient_data = [{'name': i.name, 'quantity_type': i.quantity_type, 'quantity': i.quantity} for i in ingredients]

    steps = edit_recipe.step_set.all()
    steps_data = [{'description': s.description, 'order': s.order} for s in steps]

    if request.POST:
        recipe_form = RecipeForm(request.POST, instance=edit_recipe)

        ingredient_formset = IngredientFormSet(request.POST, prefix='ingr')
        steps_formset = StepFormSet(request.POST, prefix='steps')

        if recipe_form.is_valid() and ingredient_formset.is_valid() and steps_formset.is_valid():
            recipe = recipe_form.save()
            recipe.ingredient_set.all().delete()
            recipe.step_set.all().delete()

            for ingr_form in ingredient_formset.forms:
                if ingr_form.is_valid() and ingr_form.has_changed():
                    ingr = ingr_form.save(commit=False)
                    ingr.rid_id = recipe.rid
                    ingr.save()

            for steps_form in steps_formset.forms:
                if steps_form.is_valid() and steps_form.has_changed():
                    step = steps_form.save(commit=False)
                    step.rid_id = recipe.rid
                    step.save()

        return HttpResponseRedirect('/recipes/' + str(rid))
    else:
        recipe_form = RecipeForm(instance=edit_recipe)
        ingredients_formset = IngredientFormSet(initial=ingredient_data, prefix='ingr')
        steps_formset = StepFormSet(initial=steps_data, prefix='steps')
        context = {'recipe_form': recipe_form, 'rid': rid, 'ingredients_formset': ingredients_formset, 'steps_formset': steps_formset}

    return render(request, 'recipes/edit.html', context)


@login_required(login_url='/login/')
def delete(request, rid):
    delete = Recipe.objects.filter(pk=rid).delete()
    return render(request, 'recipes/delete.html')
