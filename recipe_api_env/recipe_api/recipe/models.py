from django.db import models

class Recipe(models.Model):
    name = models.CharField(unique=True, max_length=300)
    description = models.TextField()
    cooking_instructions = models.TextField()
    slug = models.SlugField()
    preparation_time = models.IntegerField(help_text='Preparation time in minutes')
    cooking_time = models.IntegerField(help_text='Cooking time in minutes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.name



class Ingredient(models.Model):
    name = models.CharField(unique=True, max_length=300)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    measurement = models.CharField(max_length=150)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='ingredients')


    def __str__(self) -> str:
        return self.name
