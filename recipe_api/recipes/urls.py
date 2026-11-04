from django.urls import path
from .views import RecipeView, RecipeDetailView

urlpatterns = [
    path('recipes/', RecipeView.as_view()),
    path('recipes/<int:id>/', RecipeDetailView.as_view()),
]