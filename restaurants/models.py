from django.db import models
from django.utils.text import slugify

class Restaurant(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class RestaurantInfo(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, related_name="info")
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    opening_hours = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Restaurants info"

    def __str__(self):
        return f"Information for {self.restaurant.name}"
