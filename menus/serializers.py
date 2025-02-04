from rest_framework import serializers
from menus.models import Menu, Category, Subcategory, Dish, Extra, DishExtra

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'slug']

class SubcategorySerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Subcategory
        fields = ['name', 'slug', 'dishes']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'slug', 'subcategories', 'dishes']

class MenuSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    language = serializers.CharField(source='language.code', read_only=True)

    class Meta:
        model = Menu
        fields = ['name', 'language', 'slug', 'categories']