from django.contrib import admin

# Register your models here.

from .models import Recipe
from .models import Step
from .models import Ingredient
from .models import QuantityType
from .models import Category

admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Ingredient)
admin.site.register(QuantityType)
admin.site.register(Category)
