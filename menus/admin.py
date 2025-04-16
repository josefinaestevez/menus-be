from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Menu, Category, Subcategory, DishBase, Dish


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'language', 'slug')
    readonly_fields = ('slug',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'slug')
    readonly_fields = ('slug',)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug')


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'price')


class ExtraAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'slug')


class DishInline(admin.StackedInline):
    model = Dish
    extra = 1
    fields = ('name', 'description', 'category', 'subcategory')
    show_change_link = True


class DishBaseAdminForm(forms.ModelForm):
    class Meta:
        model = DishBase
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        
        if not cleaned_data.get('dishes') or cleaned_data['dishes'].count() == 0:
            raise ValidationError("A Dish must have at least one language created.")
        
        return cleaned_data
    

class DishBaseAdmin(admin.ModelAdmin):
    list_display = ('name_in_preferred_language', 'restaurant', 'price')
    inlines = [DishInline]
    form = DishBaseAdminForm

    def name_in_preferred_language(self, obj):
        ordered_translations = obj.translations.order_by('category__menu__language__code')

        english_translation = ordered_translations.filter(
            category__menu__language__code='en'
        ).first()

        if english_translation:
            return english_translation.name

        first_translation = ordered_translations.order_by('category__menu__language__code').first()
        if first_translation:
            return first_translation.name

        return "No Translation Available"
    
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
