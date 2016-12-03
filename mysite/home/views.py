from django.db.models import Q
from django.shortcuts import render

from recipes.models import Recipe, Ingredient


def index(request):
    query = request.GET.get("q")
    recipes_list = Recipe.objects.all()

    if query and request.GET:
        if "," in query:
            recipes_list = get_by_ingredient_list(query)
        else:
            recipes_list = recipes_list.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(ingredient__name__icontains=query)).distinct()

        context = {'recipes_list': recipes_list}
        return render(request, 'home/search.html', context)

    return render(request, 'home/index.html')


def get_by_ingredient_list(ingredients_str):
    ingredients_list = ingredients_str.split(",")
    map(unicode.strip, ingredients_list)

    recipes = Recipe.objects.filter()

    for ingr in ingredients_list:
        recipes = recipes.filter(ingredient__name__icontains=unicode.strip(ingr))

    recipes = recipes.distinct()

    return recipes
