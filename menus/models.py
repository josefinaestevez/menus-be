import os
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from utils.mixins import SlugMixin


class Menu(SlugMixin, models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    language = models.ForeignKey('languages.Language', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, default='Menu')
    slug = models.SlugField()

    class Meta:
        unique_together = ['restaurant', 'language', 'slug']

    def __str__(self):
        return self.name


class Category(SlugMixin, models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categories')
    slug = models.SlugField()
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'
        unique_together = ['menu', 'slug']

    def __str__(self):
        return f"{self.name} ({self.menu.language.code})"


class Subcategory(SlugMixin, models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    slug = models.SlugField()
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Subcategories'
        unique_together = ['category', 'slug']

    def __str__(self):
        return f"{self.name} ({self.category.menu.language.code})"


def dish_photo_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{instance.id}.{ext}'
    restaurant_slug = instance.restaurant.slug

    return os.path.join('media', restaurant_slug, 'dishes', new_filename)


class DishBase(models.Model):
    photo = models.ImageField(upload_to=dish_photo_upload_path, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # This field is redundant, but it'll simplify things since we don't have a restaurant yet when creating a dish base
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        english_translation = self.translations.filter(
            category__menu__language__code='en'
        ).first()
        if english_translation:
            return english_translation.name

        first_translation = self.translations.order_by('category__menu__language__code').first()
        if first_translation:
            return first_translation.name

        return f"Dish #{self.id}"  # fallback
    
    def clean(self):
        if self.pk:
            for translation in self.translations.all():
                t_restaurant = None
                if translation.category:
                    t_restaurant = translation.category.menu.restaurant
                elif translation.subcategory:
                    t_restaurant = translation.subcategory.category.menu.restaurant

                if t_restaurant and t_restaurant != self.restaurant:
                    raise ValidationError("All translations must belong to the same restaurant as the DishBase.")
    

class Dish(SlugMixin, models.Model):
    slug = models.SlugField()
    base = models.ForeignKey(DishBase, on_delete=models.CASCADE, related_name='translations')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='dishes')
    subcategory = models.ForeignKey(Subcategory, null=True, blank=True, on_delete=models.CASCADE, related_name='dishes')

    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Languages"
        constraints = [
            models.UniqueConstraint(fields=['category', 'slug'], name='unique_category_slug', condition=models.Q(category__isnull=False)),
            models.UniqueConstraint(fields=['subcategory', 'slug'], name='unique_subcategory_slug', condition=models.Q(subcategory__isnull=False)),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        if self.category:
            return self.category.menu.language.name
        elif self.subcategory:
            return self.subcategory.category.menu.language.name
        raise ValueError("Dish must have either a category or a subcategory.")


# class Extra(models.Model):
#     restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
#     slug = models.SlugField()
#     name = models.CharField(max_length=200)

#     class Meta:
#         unique_together = ['restaurant', 'slug']


# class DishExtra(models.Model):
#     dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
#     extra = models.ForeignKey(Extra, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.dish.name} + {self.extra.name}"


