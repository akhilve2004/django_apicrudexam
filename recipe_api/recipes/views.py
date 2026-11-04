from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Recipe
from .serializers import RecipeSerializer


class RecipeView(APIView):

    #GET RECIPIE
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)

        return Response(serializer.data)
    #ADD RECIPIE
    def post(self, request):

        serializer = RecipeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetailView(APIView):

    def get(self, request, id):

        recipe = get_object_or_404(Recipe, id=id)
        serializer = RecipeSerializer(recipe)

        return Response(serializer.data)

    #UPDATE
    def put(self, request, id):

        recipe = get_object_or_404(Recipe, id=id)
        serializer = RecipeSerializer(recipe, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id):

        recipe = get_object_or_404(Recipe, id=id)
        serializer = RecipeSerializer(
            recipe,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


      #DELETE
    def delete(self, request, id):

        recipe = get_object_or_404(Recipe, id=id)
        recipe.delete()

        return Response(
            {"message": "Recipe deleted successfully"},
            status=status.HTTP_200_OK
        )
