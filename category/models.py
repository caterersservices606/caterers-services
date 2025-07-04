from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    positions = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    
class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    item = models.OneToOneField(Item, related_name="recipe", on_delete=models.CASCADE)
    ingredients = models.JSONField(default=dict)  # Stores ingredients as a JSON object

    def __str__(self):
        return f"Ingredients for {self.item.name}"
