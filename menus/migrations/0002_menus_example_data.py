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
    DishBase = apps.get_model("menus", "DishBase")  # DishBase model
    Dish = apps.get_model("menus", "Dish")  # Dish model
    Language = apps.get_model('languages', 'Language')

    # Retrieve the 'Sunny Bites' restaurant
    restaurant = Restaurant.objects.filter(slug="sunny-bites").first()
    if not restaurant:
        return  # If the restaurant does not exist, exit

    es = Language.objects.get(code='es')
    en = Language.objects.get(code='en')

    # Create menu in Spanish
    menu_es = Menu.objects.create(
        restaurant=restaurant, 
        name="Menú",
        language=es,
        slug="menu-es"
    )

    # Create menu in English
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

    # Create the DishBase instances (photo, price, restaurant)
    dishbase = [
        DishBase(price=5.00),
        DishBase(price=7.50),
        DishBase(price=6.00),
        DishBase(price=12.50),
        DishBase(price=14.00),
        DishBase(price=2.00),
        DishBase(price=3.00),
        DishBase(price=3.00),
        DishBase(price=7.00),
        DishBase(price=6.50),
    ]
    
    # Create the DishBase instances and save them
    dishbases = DishBase.objects.bulk_create(dishbase)

    # Create dishes in Spanish
    dishes_es = [
        Dish(category=starters_es, base=dishbases[0], name='Bruschetta', description='Pan con tomate y albahaca', slug=slugify('Bruschetta')),
        Dish(category=starters_es, base=dishbases[1], name='Empanadas', description='Rellenas de carne o queso', slug=slugify('Empanadas')),
        Dish(category=starters_es, base=dishbases[2], name='Gazpacho', description='Sopa fría de tomate', slug=slugify('Gazpacho')),
        Dish(category=mains_es, base=dishbases[3], name='Milanesa con puré', description='Carne empanada con puré de papas', slug=slugify('Milanesa con puré')),
        Dish(category=mains_es, base=dishbases[4], name='Paella', description='Arroz con mariscos', slug=slugify('Paella')),
        Dish(category=drinks_es, base=dishbases[5], name='Agua mineral', description='Agua embotellada', slug=slugify('Agua mineral')),
        Dish(subcategory=soft_drinks_es, base=dishbases[6], name='Coca Cola', description='Refresco de cola', slug=slugify('Coca Cola')),
        Dish(subcategory=soft_drinks_es, base=dishbases[7], name='Fanta', description='Refresco de naranja', slug=slugify('Fanta')),
        Dish(subcategory=cocktails_es, base=dishbases[8], name='Mojito', description='Cóctel de ron, menta y limón', slug=slugify('Mojito')),
        Dish(subcategory=cocktails_es, base=dishbases[9], name='Margarita', description='Cóctel de tequila y lima', slug=slugify('Margarita')),
    ]

    # Create dishes in English
    dishes_en = [
        Dish(category=starters_en, base=dishbases[0], name='Bruschetta', description='Bread with tomato and basil', slug=slugify('Bruschetta')),
        Dish(category=starters_en, base=dishbases[1], name='Empanadas', description='Stuffed with meat or cheese', slug=slugify('Empanadas')),
        Dish(category=starters_en, base=dishbases[2], name='Gazpacho', description='Cold tomato soup', slug=slugify('Gazpacho')),
        Dish(category=mains_en, base=dishbases[3], name='Breaded Meat with Mash', description='Breaded meat with mashed potatoes', slug=slugify('Breaded Meat with Mash')),
        Dish(category=mains_en, base=dishbases[4], name='Paella', description='Rice with seafood', slug=slugify('Paella')),
        Dish(category=drinks_en, base=dishbases[5], name='Mineral Water', description='Bottled water', slug=slugify('Mineral Water')),
        Dish(subcategory=soft_drinks_en, base=dishbases[6], name='Coca Cola', description='Cola drink', slug=slugify('Coca Cola')),
        Dish(subcategory=soft_drinks_en, base=dishbases[7], name='Fanta', description='Orange soda', slug=slugify('Fanta')),
        Dish(subcategory=cocktails_en, base=dishbases[8], name='Mojito', description='Rum, mint, and lime cocktail', slug=slugify('Mojito')),
        Dish(subcategory=cocktails_en, base=dishbases[9], name='Margarita', description='Tequila and lime cocktail', slug=slugify('Margarita')),
    ]

    # Bulk create dishes for both Spanish and English menus
    Dish.objects.bulk_create(dishes_es)
    Dish.objects.bulk_create(dishes_en)

class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),  # Adjust this to match your actual dependencies
    ]

    operations = [
        migrations.RunPython(create_sample_menu),
    ]
