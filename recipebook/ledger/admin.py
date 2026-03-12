from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "user") 
    search_fields = ("name",)

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "created_on")
    list_filter = ("author", "created_on")
    inlines = [RecipeIngredientInline, RecipeImageInline]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("recipe", "ingredient", "quantity")
    list_filter = ("recipe", "ingredient")



