from django.contrib import admin
from .models import Menu, Category, Subcategory, Dish, Extra, DishExtra

class MenuAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'language', 'slug')
    prepopulated_fields = {'slug': ('restaurant', 'language')}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'price')
    prepopulated_fields = {'slug': ('name',)}

class ExtraAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class DishExtraAdmin(admin.ModelAdmin):
    list_display = ('dish', 'extra', 'price')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(DishExtra, DishExtraAdmin)
