from django.urls import path
from .views import *



urlpatterns = [
    path('v1/ingredient', IngredientList),
    path('v1/ingredient/<int:Ing_id>' , IngredientDetail),
    path('v1/recipe', RecipeList),
    path('v1/recipe/<int:Rec_id>' ,RecipeDetail)
]
