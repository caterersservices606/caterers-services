from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "category"]

class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "positions",
            "items",
        ]

class CategoryPositionsChangesSerializer(serializers.Serializer):
    positions = serializers.CharField(required=True)



class RecipeIngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeIngredient
        fields = ['id', 'item', 'ingredients']

class EditRecipeIngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeIngredient
        fields = ['id', 'ingredients']