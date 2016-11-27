from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Q

from recipes.models import Recipe, Ingredient

def index(request):
    query = request.GET.get("q")
    queryset_list  = Recipe.objects.all()
    if query and request.GET:
        queryset_list = queryset_list.filter(
		    Q(title__icontains=query) | 
		    Q(description__icontains=query))
			# Still need to add ingredients searching once it can link to recipes through RID
        context = {'queryset_list': queryset_list}
        return render(request, 'home/search.html', context)
    return render(request, 'home/index.html')