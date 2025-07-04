from rest_framework import serializers
from .models import *

class IngridientsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngridientsItem
        fields = ["id", "name", "category"]


class IngridientsCategorySerializer(serializers.ModelSerializer):
    items = IngridientsItemSerializer(many=True, read_only=True)

    class Meta:
        model = IngridientsCategory
        fields = [
            "id",
            "name",
            "items",
        ]

class EventIngridientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventIngridientList
        fields = ['event_id', 'ingridient_list_data']
