from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from .models import Menu, Category, Subcategory, DishBase, Dish


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'language')
    exclude = ('slug',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'slug')
    exclude = ('slug',)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    exclude = ('slug',)


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'price')


class ExtraAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant')
    exclude = ('slug',)


class DishInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        count = 0
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                count += 1

        if count == 0:
            raise ValidationError("At least one Dish (language) is required.")
        

class DishInline(admin.StackedInline):
    model = Dish
    extra = 1
    fields = ('name', 'description', 'category', 'subcategory')
    show_change_link = True
    formset = DishInlineFormSet


class DishBaseAdminForm(forms.ModelForm):
    class Meta:
        model = DishBase
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['restaurant'].widget = forms.HiddenInput()

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        obj = form.instance
        if not obj.restaurant:
            first_translation = obj.translations.first()
            if first_translation:
                if first_translation.category:
                    obj.restaurant = first_translation.category.menu.restaurant
                elif first_translation.subcategory:
                    obj.restaurant = first_translation.subcategory.category.menu.restaurant
                obj.save()
    

class DishBaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_and_menu', 'restaurant', 'price')
    inlines = [DishInline]
    form = DishBaseAdminForm

    def name(self, obj):
        dish_translation = obj.get_preferred_translation()
        return dish_translation.name
    
    def category_and_menu(self, obj):
        dish_translation = obj.get_preferred_translation()
        if dish_translation.subcategory:
            dish_category = f"{dish_translation.subcategory.name} / {dish_translation.subcategory.category.name}"
            dish_menu = f"{dish_translation.subcategory.category.menu.name} ({dish_translation.subcategory.category.menu.language.code})"
        else:
            dish_category = dish_translation.category.name
            dish_menu = f"{dish_translation.category.menu.name} ({dish_translation.category.menu.language.code})"

        return f"{dish_category} / {dish_menu}"
    
    def restaurant(self, obj):
        if obj.translations.first().category:
            return obj.translations.first().category.menu.restaurant.name
        elif obj.translations.first().subcategory:
            return obj.translations.first().subcategory.category.menu.restaurant.name
        raise ValueError("Dish must have either a category or a subcategory.")


# class DishExtraAdmin(admin.ModelAdmin):
#     list_display = ('dish', 'extra', 'price')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(DishBase, DishBaseAdmin)
# admin.site.register(Extra, ExtraAdmin)
# admin.site.register(DishExtra, DishExtraAdmin)
