from django.db import migrations

def add_sunny_bites_info(apps, schema_editor):
    """
    Adds detailed information for the existing 'Sunny Bites' restaurant.
    """
    Restaurant = apps.get_model("restaurants", "Restaurant")
    RestaurantInfo = apps.get_model("restaurants", "RestaurantInfo")

    # Fetch the 'Sunny Bites' restaurant (assuming it already exists)
    sunny_bites = Restaurant.objects.get(slug="sunny-bites")

    # Add detailed information for 'Sunny Bites'
    RestaurantInfo.objects.create(
        restaurant=sunny_bites,
        description="Delicious meals made with fresh ingredients.",
        address="123 Sunny Street, Beach City",
        phone_number="+1 234 567 8901",
        email="contact@sunnybites.com",
        opening_hours="Mon-Fri: 9:00 AM - 9:00 PM",
        currency="EUR",
    )

class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0004_restaurantinfo_currency"),
    ]

    operations = [
        migrations.RunPython(add_sunny_bites_info),
    ]
