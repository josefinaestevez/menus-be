from rest_framework import generics
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer

class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = "slug"
