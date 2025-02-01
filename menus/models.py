from django.db import models
from django.utils.text import slugify


class Menu(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    language = models.ForeignKey('languages.Language', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, default="Menu")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        return f"Menu for {self.restaurant.name} in {self.language.name}"

class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.name

class Dish(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name

class Extra(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class DishExtra(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    extra = models.ForeignKey(Extra, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.dish.name} + {self.extra.name}"


