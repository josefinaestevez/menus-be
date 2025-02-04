from django.db import migrations
from django.utils.text import slugify

def create_sample_menu(apps, schema_editor):
    """
    Creates a sample menu for 'Sunny Bites' with categories, subcategories, and dishes in Spanish and English.
    """
    Restaurant = apps.get_model("restaurants", "Restaurant")
    Menu = apps.get_model("menus", "Menu")
    Category = apps.get_model("menus", "Category")
    Subcategory = apps.get_model("menus", "Subcategory")
    Dish = apps.get_model("menus", "Dish")
    Language = apps.get_model('languages', 'Language')

    # Retrieve the 'Sunny Bites' restaurant
    restaurant = Restaurant.objects.filter(slug="sunny-bites").first()
    if not restaurant:
        return  # If the restaurant does not exist, exit

    es = Language.objects.get(code='es')
    en = Language.objects.get(code='en')

    # Create menus in Spanish
    menu_es = Menu.objects.create(
        restaurant=restaurant, 
        name="Menú",
        language=es,
        slug="menu-es"
    )

    # Create menus in English
    menu_en = Menu.objects.create(
        restaurant=restaurant, 
        name="Menu",
        language=en,
        slug="menu-en"
    )

    # Create categories in Spanish
    starters_es = Category.objects.create(menu=menu_es, name='Entradas', slug=slugify('Entradas'))
    mains_es = Category.objects.create(menu=menu_es, name='Platos principales', slug=slugify('Platos principales'))
    drinks_es = Category.objects.create(menu=menu_es, name='Bebidas', slug=slugify('Bebidas'))

    # Create categories in English
    starters_en = Category.objects.create(menu=menu_en, name='Starters', slug=slugify('Starters'))
    mains_en = Category.objects.create(menu=menu_en, name='Mains', slug=slugify('Mains'))
    drinks_en = Category.objects.create(menu=menu_en, name='Drinks', slug=slugify('Drinks'))

    # Create subcategories under 'Bebidas' and 'Drinks'
    soft_drinks_es = Subcategory.objects.create(name='Refrescos', slug=slugify('Refrescos'), category=drinks_es)
    cocktails_es = Subcategory.objects.create(name='Cócteles', slug=slugify('Cócteles'), category=drinks_es)

    soft_drinks_en = Subcategory.objects.create(name='Soft Drinks', slug=slugify('Soft Drinks'), category=drinks_en)
    cocktails_en = Subcategory.objects.create(name='Cocktails', slug=slugify('Cocktails'), category=drinks_en)

    # Create dishes for categories in Spanish
    dishes_es = [
        # Dishes in Starters category
        Dish(category=starters_es, name='Bruschetta', description='Pan con tomate y albahaca', price=5.00, slug=slugify('Bruschetta')),
        Dish(category=starters_es, name='Empanadas', description='Rellenas de carne o queso', price=7.50, slug=slugify('Empanadas')),
        Dish(category=starters_es, name='Gazpacho', description='Sopa fría de tomate', price=6.00, slug=slugify('Gazpacho')),
        Dish(category=starters_es, name='Ensalada César', description='Lechuga, pollo y aderezo César', price=8.00, slug=slugify('Ensalada César')),

        # Dishes in Mains category
        Dish(category=mains_es, name='Milanesa con puré', description='Carne empanada con puré de papas', price=12.50, slug=slugify('Milanesa con puré')),
        Dish(category=mains_es, name='Paella', description='Arroz con mariscos', price=14.00, slug=slugify('Paella')),
        Dish(category=mains_es, name='Asado', description='Carne a la parrilla', price=18.00, slug=slugify('Asado')),
        Dish(category=mains_es, name='Pasta Alfredo', description='Pasta con salsa cremosa', price=11.00, slug=slugify('Pasta Alfredo')),

        # Dishes in Drinks category (main category)
        Dish(category=drinks_es, name='Agua mineral', description='Agua embotellada', price=2.00, slug=slugify('Agua mineral')),

        # Dishes in subcategories
        Dish(subcategory=soft_drinks_es, name='Coca Cola', description='Refresco de cola', price=3.00, slug=slugify('Coca Cola')),
        Dish(subcategory=soft_drinks_es, name='Fanta', description='Refresco de naranja', price=3.00, slug=slugify('Fanta')),
        Dish(subcategory=cocktails_es, name='Mojito', description='Cóctel de ron, menta y limón', price=7.00, slug=slugify('Mojito')),
        Dish(subcategory=cocktails_es, name='Margarita', description='Cóctel de tequila y lima', price=6.50, slug=slugify('Margarita')),
    ]

    # Create dishes for categories in English
    dishes_en = [
        # Dishes in Starters category
        Dish(category=starters_en, name='Bruschetta', description='Bread with tomato and basil', price=5.00, slug=slugify('Bruschetta')),
        Dish(category=starters_en, name='Empanadas', description='Stuffed with meat or cheese', price=7.50, slug=slugify('Empanadas')),
        Dish(category=starters_en, name='Gazpacho', description='Cold tomato soup', price=6.00, slug=slugify('Gazpacho')),
        Dish(category=starters_en, name='Caesar Salad', description='Lettuce, chicken, and Caesar dressing', price=8.00, slug=slugify('Caesar Salad')),

        # Dishes in Mains category
        Dish(category=mains_en, name='Breaded Beef with mashed potatoes', description='Breaded meat with mashed potatoes', price=12.50, slug=slugify('Breaded Beef with mashed potatoes')),
        Dish(category=mains_en, name='Paella', description='Rice with seafood', price=14.00, slug=slugify('Paella')),
        Dish(category=mains_en, name='Grilled Meat', description='Grilled meat', price=18.00, slug=slugify('Grilled Meat')),
        Dish(category=mains_en, name='Pasta Alfredo', description='Pasta with creamy sauce', price=11.00, slug=slugify('Pasta Alfredo')),

        # Dishes in Drinks category (main category)
        Dish(category=drinks_en, name='Mineral Water', description='Bottled water', price=2.00, slug=slugify('Mineral Water')),

        # Dishes in subcategories
        Dish(subcategory=soft_drinks_en, name='Coca Cola', description='Cola soda', price=3.00, slug=slugify('Coca Cola')),
        Dish(subcategory=soft_drinks_en, name='Fanta', description='Orange soda', price=3.00, slug=slugify('Fanta')),
        Dish(subcategory=cocktails_en, name='Mojito', description='Rum, mint, and lime cocktail', price=7.00, slug=slugify('Mojito')),
        Dish(subcategory=cocktails_en, name='Margarita', description='Tequila and lime cocktail', price=6.50, slug=slugify('Margarita')),
    ]

    Dish.objects.bulk_create(dishes_es + dishes_en)


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_alter_category_slug_alter_dish_slug_alter_extra_slug_and_more'),
        ('restaurants', '0003_add_example_restaurant'),
        ('languages', '0003_populate_languages')
    ]

    operations = [
        migrations.RunPython(create_sample_menu),
    ]
