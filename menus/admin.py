from django.contrib import admin
from .models import Menu, Category, Subcategory, Dish, Extra, DishExtra

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

class DishExtraAdmin(admin.ModelAdmin):
    list_display = ('dish', 'extra', 'price')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(DishExtra, DishExtraAdmin)
