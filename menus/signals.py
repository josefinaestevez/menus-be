from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Menu, Category, Subcategory, Dish

def generate_unique_slug(instance, model, filter_conditions):
    """Generates a unique slug for the given model and filter conditions."""
    if not instance.slug:
        base_slug = slugify(instance.name)
        slug = base_slug
        counter = 1
        while model.objects.filter(**filter_conditions, slug=slug).exists():
            counter += 1
            slug = f"{base_slug}-{counter}"
        instance.slug = slug

@receiver(pre_save, sender=Menu)
def set_menu_slug_before_save(sender, instance, **kwargs):
    generate_unique_slug(instance, Menu, {'restaurant': instance.restaurant, 'language': instance.language})

@receiver(pre_save, sender=Category)
def set_category_slug_before_save(sender, instance, **kwargs):
    generate_unique_slug(instance, Category, {'menu': instance.menu})

@receiver(pre_save, sender=Subcategory)
def set_subcategory_slug_before_save(sender, instance, **kwargs):
    generate_unique_slug(instance, Subcategory, {'category': instance.category})

@receiver(pre_save, sender=Dish)
def set_dish_slug_before_save(sender, instance, **kwargs):
    generate_unique_slug(instance, Dish, {'category': instance.category, 'subcategory': instance.subcategory})
