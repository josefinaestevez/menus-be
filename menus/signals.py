from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Menu, Category, Subcategory, Dish

@receiver(pre_save, sender=Menu)
def set_menu_slug_before_save(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(f"{instance.name}-{instance.language.code}")
        slug = base_slug
        counter = 1
        while Menu.objects.filter(restaurant=instance.restaurant, slug=slug).exists():
            counter += 1
            slug = f"{base_slug}-{counter}"
        instance.slug = slug

@receiver(pre_save, sender=Category)
def set_category_slug_before_save(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.name)
        slug = base_slug
        counter = 1
        while Category.objects.filter(menu=instance.menu, slug=slug).exists():
            counter += 1
            slug = f"{base_slug}-{counter}"
        instance.slug = slug

@receiver(pre_save, sender=Subcategory)
def set_subcategory_slug_before_save(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.name)
        slug = base_slug
        counter = 1
        while Subcategory.objects.filter(menu=instance.menu, slug=slug).exists():
            counter += 1
            slug = f"{base_slug}-{counter}"
        instance.slug = slug

@receiver(pre_save, sender=Dish)
def set_dish_slug_before_save(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.name)
        slug = base_slug
        counter = 1
        while Dish.objects.filter(category=instance.category, subcategory=instance.subcategory, slug=slug).exists():
            counter += 1
            slug = f"{base_slug}-{counter}"
        instance.slug = slug
