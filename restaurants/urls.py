from django.urls import path
from .views import RestaurantDetailView

urlpatterns = [
    path('<slug:slug>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
]