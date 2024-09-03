from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, MealTime, Day, DayMeal


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'proteins', 'fats', 'carbs', 'calories')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(MealTime)
admin.site.register(Day)
admin.site.register(DayMeal)