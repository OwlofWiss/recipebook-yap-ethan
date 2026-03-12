from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import Recipe, RecipeImage

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
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name'] 
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ['image', 'description']
    template_name = "recipes/image_form.html"

    def form_valid(self, form):
        recipe_pk = self.kwargs.get('pk')
        form.instance.recipe = get_object_or_404(Recipe, pk=recipe_pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, pk=self.kwargs.get('pk'))
        return context

