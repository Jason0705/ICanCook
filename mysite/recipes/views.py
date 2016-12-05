from urllib import quote_plus

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from django.forms import formset_factory
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from .forms import RecipeForm, CategoryForm, StepForm, IngredientForm, BaseIngredientFormSet, BaseStepsFormSet
from .models import Recipe, Category


def index(request):
    recipe_names = Recipe.objects.all()  # .order_by('-created')

    # paginator = Paginator(recipe_names_list, 6)  # Show 10 recipes per page
    #
    # page = request.GET.get('page')
    # try:
    #     recipe_names = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     recipe_names = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     recipe_names = paginator.page(paginator.num_pages)

    context = {'recipe_names': recipe_names}

    return render(request, 'recipes/index.html', context)


def quick(request):
    quick_recipes = Recipe.objects.filter(prep_time__lte=15)

    # paginator = Paginator(quick_recipes, 10)  # Show 10 contacts per page
    #
    # page = request.GET.get('page')
    # try:
    #     recipe_names = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     recipe_names = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     recipe_names = paginator.page(paginator.num_pages)
    #
    # context = {'recipe_names': recipe_names}
    context = {'recipe_names': quick_recipes}

    return render(request, 'recipes/quick.html', context)


def lowcal(request):
    lowcal_recipes = Recipe.objects.filter(calorie__lte=350)

    # paginator = Paginator(lowcal_recipes, 10)  # Show 10 contacts per page
    #
    # page = request.GET.get('page')
    # try:
    #     recipe_names = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     recipe_names = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     recipe_names = paginator.page(paginator.num_pages)

    # context = {'recipe_names': recipe_names}
    context = {'recipe_names': lowcal_recipes}

    return render(request, 'recipes/lowcal.html', context)


def breakfast(request):
    breakfast_recipes = Category.objects.filter(breakfast=True)

    # paginator = Paginator(breakfast_recipes, 10)  # Show 10 contacts per page
    #
    # page = request.GET.get('page')
    # try:
    #     recipe_names = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     recipe_names = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     recipe_names = paginator.page(paginator.num_pages)
    #
    # context = {'recipe_names': recipe_names}
    context = {'recipe_names': breakfast_recipes}

    return render(request, 'recipes/breakfast.html', context)


def lunch(request):
    lunch_recipes = Category.objects.filter(lunch=True)

    # paginator = Paginator(lunch_recipes, 10)  # Show 10 contacts per page
    #
    # page = request.GET.get('page')
    # try:
    #     recipe_names = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     recipe_names = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     recipe_names = paginator.page(paginator.num_pages)
    #
    # context = {'recipe_names': recipe_names}
    context = {'recipe_names': lunch_recipes}

    return render(request, 'recipes/lunch.html', context)


def dinner(request):
    dinner_recipes = Category.objects.filter(dinner=True)

    # paginator = Paginator(dinner_recipes, 10)  # Show 10 contacts per page
    #
    # page = request.GET.get('page')
    # try:
    #     recipe_names = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     recipe_names = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     recipe_names = paginator.page(paginator.num_pages)
    #
    # context = {'recipe_names': recipe_names}
    context = {'recipe_names': dinner_recipes}

    return render(request, 'recipes/dinner.html', context)


def dessert(request):
    dessert_recipes = Category.objects.filter(dessert=True)

    # paginator = Paginator(dessert_recipes, 10)  # Show 10 contacts per page
    #
    # page = request.GET.get('page')
    # try:
    #     recipe_names = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     recipe_names = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     recipe_names = paginator.page(paginator.num_pages)

    # context = {'recipe_names': recipe_names}
    context = {'recipe_names': dessert_recipes}

    return render(request, 'recipes/dessert.html', context)


def holiday(request):
    holiday_recipes = Category.objects.filter(holiday=True)

    # paginator = Paginator(holiday_recipes, 10)  # Show 10 contacts per page
    #
    # page = request.GET.get('page')
    # try:
    #     recipe_names = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     recipe_names = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     recipe_names = paginator.page(paginator.num_pages)

    # context = {'recipe_names': recipe_names}
    context = {'recipe_names': holiday_recipes}

    return render(request, 'recipes/holiday.html', context)


def details(request, rid):
    try:
        recipe = Recipe.objects.get(pk=rid)
        current_user = request.user
        user_id = current_user.id
        favourited = Recipe.objects.filter(favourites=user_id, pk=rid)
        user = User.objects.get(id=recipe.userid)

        name = "{0} {1}".format(user.first_name, user.last_name)
        share_string = quote_plus(recipe.description)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist.")

    if recipe.recipe_pic is None:
        recipe.recipe_pic = ""

    context = {
        'recipe': recipe,
        'share_string': share_string,
        'favourited': favourited,
        'user_full_name': name
    }
    return render(request, 'recipes/details.html', context)


def tips(request):
    return render(request, 'recipes/tips.html')


def healthy_living(request):
    return render(request, 'recipes/healthy_living.html')


def nutrition_guide(request):

    return render(request, 'recipes/nutrition_guide.html')


@login_required(login_url='/login/')
def add_recipe(request):
    StepFormSet = formset_factory(StepForm, formset=BaseStepsFormSet)
    IngredientFormSet = formset_factory(IngredientForm, formset=BaseIngredientFormSet)

    recipe_form = RecipeForm()
    category_form = CategoryForm()
    ingredients_formset = IngredientFormSet(prefix='ingr')
    steps_formset = StepFormSet(prefix='steps')

    if request.POST:
        recipe_form = RecipeForm(request.POST)
        category_form = CategoryForm(request.POST)

        ingredients_formset = IngredientFormSet(request.POST, prefix='ingr')
        steps_formset = StepFormSet(request.POST, prefix='steps')

        if recipe_form.is_valid() and category_form.is_valid() and ingredients_formset.is_valid() and steps_formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.userid = request.user.id
            recipe.created = datetime.now()
            recipe.save()

            category = category_form.save(commit=False)
            category.rid_id = recipe.rid
            category.save()

            for ingr_form in ingredients_formset.forms:
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

    context = {'recipe_form': recipe_form, 'category_form': category_form, 'ingredients_formset': ingredients_formset, 'steps_formset': steps_formset}
    return render(request, 'recipes/add.html', context)


@transaction.atomic
@login_required(login_url='/login/')
def edit(request, rid):
    edit_recipe = Recipe.objects.get(pk=rid)

    if request.user.id != edit_recipe.userid:
        return render(request, 'global/not_authorized.html')

    StepFormSet = formset_factory(StepForm, formset=BaseStepsFormSet)
    IngredientFormSet = formset_factory(IngredientForm, formset=BaseIngredientFormSet)

    ingredients = edit_recipe.ingredient_set.all()
    ingredient_data = [{'name': i.name, 'quantity_type': i.quantity_type, 'quantity': i.quantity} for i in ingredients]

    steps = edit_recipe.step_set.all()
    steps_data = [{'description': s.description, 'order': s.order} for s in steps]

    categories = Category.objects.get(rid=rid)
    category_data = {'breakfast': categories.breakfast, 'lunch': categories.lunch, 'dinner': categories.dinner, 'dessert': categories.dessert,
                     'holiday': categories.holiday}

    if request.POST:
        recipe_form = RecipeForm(request.POST, request.FILES, instance=edit_recipe)
        category_form = CategoryForm(request.POST, instance=categories)

        ingredients_formset = IngredientFormSet(request.POST, prefix='ingr')
        steps_formset = StepFormSet(request.POST, prefix='steps')

        if recipe_form.is_valid() and category_form.is_valid() and ingredients_formset.is_valid() and steps_formset.is_valid():
            recipe = recipe_form.save()
            recipe.ingredient_set.all().delete()
            recipe.step_set.all().delete()

            category = category_form.save(commit=False)
            category.rid_id = recipe.rid
            category.save()

            for ingr_form in ingredients_formset.forms:
                if ingr_form.is_valid() and ingr_form.has_changed():
                    ingr = ingr_form.save(commit=False)
                    ingr.rid_id = recipe.rid
                    ingr.save()

            for steps_form in steps_formset.forms:
                if steps_form.is_valid() and steps_form.has_changed():
                    step = steps_form.save(commit=False)
                    step.rid_id = recipe.rid
                    step.save()

            recipe.save()

            return HttpResponseRedirect('/recipes/' + str(rid))

        else:
            context = {'recipe_form': recipe_form, 'category_form': category_form, 'rid': rid, 'ingredients_form': ingredients_formset,
                       'steps_formset': steps_formset}
            return render(request, 'recipes/edit.html', context)

    else:
        recipe_form = RecipeForm(instance=edit_recipe)
        category_form = CategoryForm(instance=categories, initial=category_data)
        ingredients_formset = IngredientFormSet(initial=ingredient_data, prefix='ingr')
        steps_formset = StepFormSet(initial=steps_data, prefix='steps')
        context = {'recipe_form': recipe_form, 'category_form': category_form, 'rid': rid, 'ingredients_formset': ingredients_formset,
                   'steps_formset': steps_formset}

    return render(request, 'recipes/edit.html', context)


@login_required(login_url='/login/')
def delete(request, rid):
    delete = Recipe.objects.filter(pk=rid).delete()
    return render(request, 'recipes/delete.html')


@login_required(login_url='/login/')
def remove(request, rid):
    current_user = request.user
    user_id = current_user.id
    favourited_recipe = Recipe.objects.filter(favourites=user_id, pk=rid)
    for recipe in favourited_recipe:
        recipe.favourites.remove(current_user)
    context = {'rid': rid}
    return render(request, 'recipes/remove.html', context)


@login_required(login_url='/login/')
def favourite(request, rid):
    current_user = request.user
    user_id = current_user.id
    favourited_recipe = Recipe.objects.filter(pk=rid)
    for recipe in favourited_recipe:
        recipe.favourites.add(current_user)
    context = {'rid': rid}
    return render(request, 'recipes/favourite.html', context)
