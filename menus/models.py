from django.db import models
from django.utils.text import slugify


class Menu(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    language = models.ForeignKey('languages.Language', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, default='Menu')
    slug = models.SlugField()

    class Meta:
        unique_together = ['restaurant', 'language', 'slug']

    def __str__(self):
        return self.name

class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categories')
    slug = models.SlugField()
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'
        unique_together = ['menu', 'slug']

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    slug = models.SlugField()
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Subcategories'
        unique_together = ['category', 'slug']

    def __str__(self):
        return self.name

class Dish(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='dishes')
    subcategory = models.ForeignKey(Subcategory, null=True, blank=True, on_delete=models.CASCADE, related_name='dishes')
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Dishes'
        constraints = [
            # Ensures that the slug is unique per category or per subcategory
            models.UniqueConstraint(fields=['category', 'slug'], name='unique_category_slug', condition=models.Q(category__isnull=False)),
            models.UniqueConstraint(fields=['subcategory', 'slug'], name='unique_subcategory_slug', condition=models.Q(subcategory__isnull=False)),
        ]
    
    def __str__(self):
        return self.name

class Extra(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    slug = models.SlugField()
    name = models.CharField(max_length=200)

    class Meta:
        unique_together = ['restaurant', 'slug']

class DishExtra(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    extra = models.ForeignKey(Extra, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.dish.name} + {self.extra.name}"


