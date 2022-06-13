from rest_framework import serializers
from .models import Ingredient, Recipe



class IngredientSerializer(serializers.ModelSerializer):

 
    class Meta: 
        model = Ingredient
        fields = ('name', 'amount', 'measurement', 'recipe')

class RecipeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Recipe
        fields = ('slug', 'name', 'description', 'cooking_instructions',
            'cooking_time', 'preparation_time',
            'created', 'updated')

