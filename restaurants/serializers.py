from rest_framework import serializers
from restaurants.models import Restaurant, RestaurantInfo
from menus.serializers import MenuSerializer

class RestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantInfo
        fields = ['description', 'address', 'phone_number', 'email', 'opening_hours']

class RestaurantSerializer(serializers.ModelSerializer):
    info = RestaurantInfoSerializer(read_only=True)
    menus = MenuSerializer(many=True, read_only=True, source="menu_set")

    class Meta:
        model = Restaurant
        fields = ['name', 'slug', 'info', 'menus']
