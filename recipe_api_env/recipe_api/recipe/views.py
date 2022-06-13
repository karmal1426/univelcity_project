from rest_framework import response
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import  IngredientSerializer, RecipeSerializer
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

      #####INGREDIENT VIEW TO PERFORM CRUD FOR ONE OR ALL DATA#####

@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication, SessionAuthentication, ])
@permission_classes([IsAuthenticated])
def IngredientList(request):
    if request.method == 'GET':
        get_ingredient = Ingredient.objects.all()
        serializer = IngredientSerializer(get_ingredient, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # serializer.validated_data['password'] = make_password(serializer.validated_data['password']) #hash the password and set it as the password
            # new_user = Ingredient.objects.create(**serializer.validated_data) #create a new user
            # serializer = IngredientSerializer(new_user) #serialize the user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # returned response

        else:#if data is not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Ingredient.delete




@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication, SessionAuthentication, ])
@permission_classes([IsAuthenticatedOrReadOnly])
def IngredientDetail(request, Ing_id):
    try:
        ingredient_id = Ingredient.objects.get(id=Ing_id)
    except Ingredient.DoesNotExist:
        return response({"message": "Ingredient does not exist"})
    if request.method == 'GET':
        serializer= IngredientSerializer(ingredient_id)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
         serializer= IngredientSerializer(ingredient_id, data=request.data, partial=True)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
         else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




     #####RECIPE VIEW TO PERFORM CRUD FOR ONE OR ALL DATA#####


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([BasicAuthentication, SessionAuthentication, ])
@permission_classes([IsAuthenticated])
def RecipeList(request):
    if request.method == 'GET':
        get_ingredient = Recipe.objects.all()
        serializer = RecipeSerializer(get_ingredient, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # returned response

        else:#if data is not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Recipe.delete




@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication, SessionAuthentication, ])
@permission_classes([IsAuthenticatedOrReadOnly])
def RecipeDetail(request, Rec_id):
    try:
        recipe_id = Recipe.objects.get(id=Rec_id)
    except Recipe.DoesNotExist:
        return response({"message": "Ingredient does not exist"})
    if request.method == 'GET':
        serializer= RecipeSerializer(recipe_id)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
         serializer= RecipeSerializer(recipe_id, data=request.data, partial=True)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
         else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


