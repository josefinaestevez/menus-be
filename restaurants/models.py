import os
from django.db import models
from django.utils.text import slugify

def restaurant_cover_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join('media/restaurants/', instance.slug, f'cover.{ext}')


class Restaurant(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    photo = models.ImageField(upload_to=restaurant_cover_upload_path, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class RestaurantInfo(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, related_name='info')
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    opening_hours = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=3, default='EUR')

    class Meta:
        verbose_name_plural = 'Restaurants info'

    def __str__(self):
        return f'Information for {self.restaurant.name}'
    

class SocialMedia(models.Model):
    PLATFORM_CHOICES = [
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('TikTok', 'TikTok'),
        ('Twitter', 'Twitter'),  # You can add more platforms if needed
    ]

    platform_name = models.CharField(
        max_length=50,
        choices=PLATFORM_CHOICES,  # Restrict the options to the predefined choices
    )
    username = models.CharField(max_length=255) # Store the username only
    restaurant = models.ForeignKey(Restaurant, related_name='social_media', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.platform_name} - {self.restaurant.name}'
