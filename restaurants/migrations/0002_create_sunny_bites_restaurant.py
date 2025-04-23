from django.db import migrations


def create_sunny_bites_restaurant(apps, schema_editor):
    Restaurant = apps.get_model('restaurants', 'Restaurant')
    RestaurantInfo = apps.get_model('restaurants', 'RestaurantInfo')
    SocialMedia = apps.get_model('restaurants', 'SocialMedia')

    restaurant = Restaurant.objects.create(
        name="Sunny Bites",
        slug="sunny-bites",
    )

    RestaurantInfo.objects.create(
        restaurant=restaurant,
        address="Calle de la Aurora, 25, 28010 Madrid, España.",
        opening_hours=(
            "Lunes a viernes: 8:30 AM - 4:00 PM"
            "Sábado y domingo: 9:00 AM - 5:00 PM"
        ),
        phone_number="+34 912 345 678",
        email="contacto@sunnybites.com",
        currency="EUR",
    )

    SocialMedia.objects.create(
        restaurant=restaurant,
        platform_name="Instagram",
        username="@sunnybites"
    )
    SocialMedia.objects.create(
        restaurant=restaurant,
        platform_name="Facebook",
        username="Sunny Bites"
    )
    SocialMedia.objects.create(
        restaurant=restaurant,
        platform_name="TikTok",
        username="@sunnybites"
    )


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sunny_bites_restaurant),
    ]
