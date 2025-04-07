# views.py

from rest_framework import generics
from rest_framework.response import Response
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer
from rest_framework.exceptions import NotFound

class RestaurantDetailView(generics.RetrieveAPIView):
    serializer_class = RestaurantSerializer
    lookup_field = "slug"

    def get_queryset(self):
        """
        Filters the queryset by restaurant slug.
        """

        # Get the restaurant based on the slug
        queryset = Restaurant.objects.filter(slug=self.kwargs['slug'])
        
        # If the restaurant doesn't exist, raise a NotFound exception
        if not queryset.exists():
            raise NotFound(detail="Restaurant not found")
        
        return queryset

    def retrieve(self, request, *args, **kwargs):
        """
        Override the 'retrieve' method to handle custom logic and return the menu.
        """
        # Get the restaurant object
        restaurant = self.get_object()

        # Get the language code from the query parameter
        lang_code = self.request.query_params.get('lang', 'en')

        # Serialize the restaurant with the language code in context
        serializer = RestaurantSerializer(restaurant, context={'lang_code': lang_code})
        return Response(serializer.data)
