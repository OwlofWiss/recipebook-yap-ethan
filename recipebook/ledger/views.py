from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Recipe

def recipe_list(request):
    
    recipes = Recipe.objects.select_related('author').all()
    
    return render(request, "recipes/list.html", {
        "recipes": recipes,
        "page_title": "Recipe List"
    })

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(
        Recipe.objects.prefetch_related('recipe_ingredients__ingredient'), 
        pk=pk
    )
    
    return render(request, "recipes/detail.html", {
        "recipe": recipe,
        "page_title": recipe.name  
    })

