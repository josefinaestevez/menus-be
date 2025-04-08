from rest_framework import serializers
from restaurants.models import Restaurant, RestaurantInfo, SocialMedia
from menus.models import Menu
from menus.serializers import MenuSerializer
from languages.models import Language


class RestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantInfo
        fields = ['description', 'address', 'phone_number', 'email', 'opening_hours', 'currency']


class SocialMediaSerializer(serializers.ModelSerializer):
    # Dynamically generate the full URL based on platform_name and username
    url = serializers.SerializerMethodField()

    class Meta:
        model = SocialMedia
        fields = ['platform_name', 'username', 'url']  # Include url to show the full URL in the response

    def get_url(self, obj):
        """
        Generate the full URL for the social media platform and username.
        """
        platform_urls = {
            'Instagram': 'https://instagram.com/',
            'Facebook': 'https://facebook.com/',
            'TikTok': 'https://tiktok.com/@',
            'Twitter': 'https://twitter.com/',
        }
        base_url = platform_urls.get(obj.platform_name)
        if base_url:
            return f"{base_url}{obj.username}"  # Combine base URL with the username
        return ""  # Return empty string if platform is not recognized


class RestaurantSerializer(serializers.ModelSerializer):
    info = RestaurantInfoSerializer(read_only=True)
    menu = serializers.SerializerMethodField()
    social_media = SocialMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['name', 'info', 'menu', 'slug', 'social_media']

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
    
