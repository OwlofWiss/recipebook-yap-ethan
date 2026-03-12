from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    name = models.CharField(max_length=50)
    short_bio = models.TextField()

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient_detail", args=[str(self.id)])

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="recipes"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_detail", args=[self.pk])

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients"
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="ingredient_recipes"
    )
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient} for {self.recipe}"
    
class RecipeImage(models.Model):
    image = models.ImageField(upload_to='recipe_images/', blank=False, null=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name="images"
    )

    def __str__(self):
        return f"Image for {self.recipe.name}"



