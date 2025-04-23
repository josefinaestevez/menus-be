from django.db import migrations
from django.utils.text import slugify


def create_menus(apps, schema_editor):
    Category = apps.get_model("menus", "Category")
    Language = apps.get_model("languages", "Language")
    Menu = apps.get_model("menus", "Menu")
    Restaurant = apps.get_model("restaurants", "Restaurant")
    Subcategory = apps.get_model("menus", "Subcategory")
    DishBase = apps.get_model("menus", "DishBase")
    Dish = apps.get_model("menus", "Dish")

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
    brunch_es = Category.objects.create(menu=menu_es, name="Brunch", slug="brunch")
    tapas_es = Category.objects.create(menu=menu_es, name="Tapas", slug="tapas")
    drinks_es = Category.objects.create(menu=menu_es, name="Bebidas", slug="bebidas")
    desserts_es = Category.objects.create(menu=menu_es, name="Postres", slug="postres")

    # Create categories in English
    brunch_en = Category.objects.create(menu=menu_en, name="Brunch", slug="brunch")
    tapas_en = Category.objects.create(menu=menu_en, name="Tapas", slug="tapas")
    drinks_en = Category.objects.create(menu=menu_en, name="Drinks", slug="drinks")
    desserts_en = Category.objects.create(menu=menu_en, name="Desserts", slug="desserts")

    # Create subcategories under 'Bebidas' and 'Drinks'
    soft_drinks_es = Subcategory.objects.create(name="Refrescos", slug="refrescos", category=drinks_es)
    cocktails_es = Subcategory.objects.create(name="Cócteles", slug="cocteles", category=drinks_es)

    soft_drinks_en = Subcategory.objects.create(name="Soft Drinks", slug="soft-drinks", category=drinks_en)
    cocktails_en = Subcategory.objects.create(name="Cócteles", slug="cocktails", category=drinks_en)

    dishes = [
        # Brunch
        {
            "base": {
                "price": 9.5
            },
            "en": {
                "name": "Continental Breakfast",
                "description": "Croissant, jam, cheese, and coffee.",
                "category": brunch_en
            },
            "es": {
                "name": "Desayuno Continental",
                "description": "Croissant, mermelada, queso y café.",
                "category": brunch_es
            }
        },
        {
            "base": {
                "price": 11
            },
            "en": {
                "name": "Avocado Brunch",
                "description": "Avocado toast, poached egg, and arugula.",
                "category": brunch_en
            },
            "es": {
                "name": "Avocado Brunch",
                "description": "Tostada de aguacate, huevo poché y rúcula.",
                "category": brunch_es
            }
        },
        {
            "base": {
                "price": 12.5
            },
            "en": {
                "name": "English Classic",
                "description": "Eggs, sausages, bacon, and beans.",
                "category": brunch_en
            },
            "es": {
                "name": "Clásico Inglés",
                "description": "Huevos, salchichas, bacon y beans.",
                "category": brunch_es
            }
        },
        {
            "base": {
                "price": 8.5
            },
            "en": {
                "name": "Smoothie Bowl",
                "description": "Fruits, yogurt, and granola.",
                "category": brunch_en
            },
            "es": {
                "name": "Smoothie Bowl",
                "description": "Frutas, yogur y granola.",
                "category": brunch_es
            }
        },
        {
            "base": {
                "price": 10.5
            },
            "en": {
                "name": "Veggie Power",
                "description": "Quinoa, spinach, tomato, and avocado.",
                "category": brunch_en
            },
            "es": {
                "name": "Veggie Power",
                "description": "Quinoa, espinacas, tomate y aguacate.",
                "category": brunch_es
            }
        },

        # Tapas
        {
            "base": {
                "price": 6.5
            },
            "en": {
                "name": "Patatas Bravas",
                "description": "Fried potatoes with spicy brava sauce.",
                "category": tapas_en
            },
            "es": {
                "name": "Patatas Bravas",
                "description": "Patatas fritas con salsa brava.",
                "category": tapas_es
            }
        },
        {
            "base": {
                "price": 7.5
            },
            "en": {
                "name": "Ham Croquettes",
                "description": "Creamy homemade croquettes.",
                "category": tapas_en
            },
            "es": {
                "name": "Croquetas de Jamón",
                "description": "CCremosas croquetas caseras.",
                "category": tapas_es
            }
        },
        {
            "base": {
                "price": 7.0
            },
            "en": {
                "name": "Spanish Omelette",
                "description": "Potato omelette with onion.",
                "category": tapas_en
            },
            "es": {
                "name": "Tortilla Española",
                "description": "Tortilla de patatas con cebolla.",
                "category": tapas_es
            }
        },
        {
            "base": {
                "price": 8.9
            },
            "en": {
                "name": "Garlic Shrimp",
                "description": "Shrimp in garlic and chili sauce.",
                "category": tapas_en
            },
            "es": {
                "name": "Gambas al Ajillo",
                "description": "Gambas en salsa de ajo y guindilla.",
                "category": tapas_es
            }
        },
        {
            "base": {
                "price": 6.5
            },
            "en": {
                "name": "Manchego Cheese",
                "description": "Piquillo peppers stuffed with cod and served with romesco sauce.",
                "category": tapas_en
            },
            "es": {
                "name": "Queso Manchego",
                "description": "Lonchas de queso curado.",
                "category": tapas_es
            }
        },

        # Desserts
        {
            "base": {
                "price": 5.5
            },
            "en": {
                "name": "Classic Cheesecake",
                "description": "Cheesecake with biscuit base.",
                "category": desserts_en
            },
            "es": {
                "name": "Cheesecake Clásico",
                "description": "Tarta de queso con base de galleta.",
                "category": desserts_es
            }
        },
        {
            "base": {
                "price": 4.9
            },
            "en": {
                "name": "Chocolate Brownie",
                "description": "Homemade brownie with walnuts.",
                "category": desserts_en
            },
            "es": {
                "name": "Brownie de Chocolate",
                "description": "Brownie casero con nueces.",
                "category": desserts_es
            }
        },
        {
            "base": {
                "price": 4.0
            },
            "en": {
                "name": "Fresh Fruit",
                "description": "Selection of seasonal fruits.",
                "category": desserts_en
            },
            "es": {
                "name": "Fruta Fresca",
                "description": "Selección de frutas de temporada.",
                "category": desserts_es
            }
        },
        {
            "base": {
                "price": 3.9
            },
            "en": {
                "name": "Artisanal Ice Cream",
                "description": "Vanilla and chocolate ice cream.",
                "category": desserts_en
            },
            "es": {
                "name": "Helado Artesanal",
                "description": "Helado de vainilla y chocolate.",
                "category": desserts_es
            }
        },
        {
            "base": {
                "price": 5.9
            },
            "en": {
                "name": "Classic Tiramisu",
                "description": "Layers of sponge cake and mascarpone.",
                "category": desserts_en
            },
            "es": {
                "name": "Tiramisú Clásico",
                "description": "Capas de bizcocho y mascarpone.",
                "category": desserts_es
            }
        },

        # Drinks
        {
            "base": {
                "price": 2
            },
            "en": {
                "name": "Espresso Coffee",
                "description": "Intense and aromatic espresso.",
                "category": drinks_en
            },
            "es": {
                "name": "Café Espresso",
                "description": "Espresso intenso y aromático.",
                "category": drinks_es
            }
        },
        {
            "base": {
                "price": 3.5
            },
            "en": {
                "name": "Fresh Orange Juice",
                "description": "Freshly squeezed orange juice.",
                "category": drinks_en
            },
            "es": {
                "name": "Zumo Natural",
                "description": "Naranja recién exprimida.",
                "category": drinks_es
            }
        },
        {
            "base": {
                "price": 4
            },
            "en": {
                "name": "Matcha Latte",
                "description": "Matcha tea with steamed milk.",
                "category": drinks_en
            },
            "es": {
                "name": "Té Matcha Latte",
                "description": "Té matcha con leche espumada.",
                "category": drinks_es
            }
        },
        {
            "base": {
                "price": 3
            },
            "en": {
                "name": "Homemade Lemonade",
                "description": "Refreshing with a touch of mint.",
                "category": drinks_en
            },
            "es": {
                "name": "Limonada Casera",
                "description": "Refrescante con toque de hierbabuena.",
                "category": drinks_es
            }
        },
        {
            "base": {
                "price": 4.5
            },
            "en": {
                "name": "Tropical Smoothie",
                "description": "Mango, pineapple, and coconut milk.",
                "category": drinks_en
            },
            "es": {
                "name": "Smoothie Tropical",
                "description": "Mango, piña y leche de coco.",
                "category": drinks_es
            }
        },
        {
            "base": {
                "price": 1.5
            },
            "en": {
                "name": "Bottled Water",
                "description": "Still or sparkling water.",
                "category": drinks_en
            },
            "es": {
                "name": "Agua embotellada",
                "description": "Agua natural o con gas.",
                "category": drinks_es
            }
        },
        {
            "base": {
                "price": 6.5
            },
            "en": {
                "name": "Mojito",
                "description": "Rum, mint, and lime cocktail.",
                "subcategory": cocktails_en
            },
            "es": {
                "name": "Mojito",
                "description": "Cóctel de ron, menta y limón.",
                "subcategory": cocktails_es
            }
        },
        {
            "base": {
                "price": 7
            },
            "en": {
                "name": "Margarita",
                "description": "Tequila and lime cocktail.",
                "subcategory": cocktails_en
            },
            "es": {
                "name": "Margarita",
                "description": "Cóctel de tequila y lima.",
                "subcategory": cocktails_es
            }
        },
        {
            "base": {
                "price": 3
            },
            "en": {
                "name": "Fanta",
                "description": "Orange soda.",
                "subcategory": soft_drinks_en
            },
            "es": {
                "name": "Fanta",
                "description": "Refresco de naranja.",
                "subcategory": soft_drinks_es
            }
        },
        {
            "base": {
                "price": 3
            },
            "en": {
                "name": "Coca Cola",
                "description": "Cola drink.",
                "subcategory": soft_drinks_en
            },
            "es": {
                "name": "Coca Cola",
                "description": "Refresco de cola.",
                "subcategory": soft_drinks_es
            }
        },
    ]

    for dish in dishes:
        base = DishBase.objects.create(
            price=dish["base"]["price"],
            restaurant=restaurant
        )
        if dish["en"].get("category"):
            # English version
            Dish.objects.create(
                base=base,
                description=dish["en"]["description"],
                category=dish["en"]["category"],
                slug=slugify(dish["en"]["name"]),
                name=dish["en"]["name"]
            )
            # Spanish version
            Dish.objects.create(
                base=base,
                description=dish["es"]["description"],
                category=dish["es"]["category"],
                slug=slugify(dish["es"]["name"]),
                name=dish["es"]["name"]
            )
        else:
            # English version
            Dish.objects.create(
                base=base,
                description=dish["en"]["description"],
                subcategory=dish["en"]["subcategory"],
                slug=slugify(dish["en"]["name"]),
                name=dish["en"]["name"]
            )
            # Spanish version
            Dish.objects.create(
                base=base,
                description=dish["es"]["description"],
                subcategory=dish["es"]["subcategory"],
                slug=slugify(dish["es"]["name"]),
                name=dish["es"]["name"]
            )



class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
        ('restaurants', '0002_create_sunny_bites_restaurant'),
    ]

    operations = [
        migrations.RunPython(create_menus),
    ]
