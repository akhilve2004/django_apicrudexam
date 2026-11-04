from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    instructions = models.TextField()
    ingredients = models.TextField()
    meal_type = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    image = models.ImageField(upload_to='recipe_images/')

    def __str__(self):
        return self.recipe_name