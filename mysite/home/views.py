from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Q

from recipes.models import Recipe, Ingredient

def index(request):
    query = request.GET.get("q")
    recipes_list  = Recipe.objects.all()
    ingredients_list = Ingredient.objects.all()
    if query and request.GET:
        recipes_list = recipes_list.filter(
		    Q(title__icontains=query) | 
		    Q(description__icontains=query)) 
        ingredients_list = ingredients_list.filter(Q(name__icontains=query))
        context = {'recipes_list': recipes_list, 'ingredients_list': ingredients_list}
        return render(request, 'home/search.html', context)
    return render(request, 'home/index.html')
