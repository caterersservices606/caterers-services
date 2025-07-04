from django.urls import path
from .views import *

urlpatterns = [
    path("categories/", CategoryViewSet.as_view()),
    path("categories/<int:pk>/", CategoryGetViewSet.as_view()),
    path("category-positions-changes/<int:pk>/",CategoryPositionsChangesViewSet.as_view()),
    path("items/", ItemViewSet.as_view()),
    path("items/<int:pk>/", ItemGetViewSet.as_view()),
    path("recipes/", RecipeIngredientViewSet.as_view()),
    path("recipes/<int:pk>/", EditRecipeIngredientViewSet.as_view()),
    path(
        "common-ingredients/",
        CommonIngredientsViewSet.as_view(),
    ),
]
