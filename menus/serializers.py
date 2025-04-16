from rest_framework import serializers
from menus.models import Menu, Category, Subcategory, Dish


class DishSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'slug', 'photo']

    def get_price(self, obj):
        return obj.base.price

    def get_photo(self, obj):
        return obj.base.photo.url if obj.base.photo else None


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