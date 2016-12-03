from django.db.models import Q
from django.shortcuts import render

from recipes.models import Recipe


def index(request):
    query = request.GET.get("q")

    if query and request.GET:
        recipes_list = None

        if "," in query:
            recipes_list = get_by_ingredient_list(query)
        else:
            recipes_list = Recipe.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query))

        context = {'recipes_list': recipes_list}
        return render(request, 'home/search.html', context)

    return render(request, 'home/index.html')


def get_by_ingredient_list(ingredients_str):
    ingredients_list = ingredients_str.split(",")
    map(unicode.strip, ingredients_list)

    recipes = Recipe.objects.filter()

    for ingr in ingredients_list:
        recipes = Recipe.objects.filter(ingredient__name__icontains=ingr)

    return recipes.values().distinct()
