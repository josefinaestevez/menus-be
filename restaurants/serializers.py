from rest_framework import serializers
from restaurants.models import Restaurant, RestaurantInfo
from menus.models import Menu
from menus.serializers import MenuSerializer
from languages.models import Language

class RestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantInfo
        fields = ['description', 'address', 'phone_number', 'email', 'opening_hours', 'currency']

class RestaurantSerializer(serializers.ModelSerializer):
    info = RestaurantInfoSerializer(read_only=True)
    menu = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['name', 'info', 'menu']

    def get_menu(self, obj):
        """
        Custom method to return the filtered menu for the specific language.
        """
        # Get the language code from the context (passed from the view)
        lang_code = self.context.get('lang_code', 'en')  # Default to 'en' if not provided
        
        try:
            language = Language.objects.get(code=lang_code)
            # Get the first menu that matches the restaurant and language
            menu = Menu.objects.filter(restaurant=obj, language=language).first()  # .first() ensures only one menu

            if menu:
                return MenuSerializer(menu).data  # Serialize and return the menu data
        except Language.DoesNotExist:
            return None  # Return None if language not found

        return None  # Return None if no matching menu is found
