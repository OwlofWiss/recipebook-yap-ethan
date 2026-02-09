from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse



def recipe_list(request):
    recipes = data["recipes"]
    return render(request, "recipes/list.html", {"recipes": recipes})

def recipe_1(request):
    recipe = data["recipes"][0]
    return render(request, "recipes/recipe1.html", {"recipe": recipe})

def recipe_2(request):
    recipe = data["recipes"][1]
    return render(request, "recipes/recipe2.html", {"recipe": recipe})

data = {
    "recipes": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {"name": "tomato", "quantity": "3pcs"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "pork", "quantity": "1kg"},
                {"name": "water", "quantity": "1L"},
                {"name": "sinigang mix", "quantity": "1 packet"},
            ],
            "link": "/recipe/1"
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {"name": "garlic", "quantity": "1 head"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "vinegar", "quantity": "1/2cup"},
                {"name": "water", "quanity": "1 cup"},  
                {"name": "salt", "quantity": "1 tablespoon"},
                {"name": "whole black peppers", "quantity": "1 tablespoon"},
                {"name": "pork", "quantity": "1 kilo"},
            ],
            "link": "/recipe/2"
        }
    ]
}