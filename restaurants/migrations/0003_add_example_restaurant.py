from django.db import migrations

def create_sunny_bites(apps, schema_editor):
    """
    Creates a sample restaurant called 'Sunny Bites'.
    """
    Restaurant = apps.get_model("restaurants", "Restaurant")  # Get the Restaurant model

    # Create the 'Sunny Bites' restaurant
    Restaurant.objects.create(
        name="Sunny Bites",
        slug="sunny-bites",
    )

class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0002_alter_restaurantinfo_options"),
    ]

    operations = [
        migrations.RunPython(create_sunny_bites),
    ]
