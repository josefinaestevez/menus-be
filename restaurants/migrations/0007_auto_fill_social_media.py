from django.db import migrations

def fill_social_media(apps, schema_editor):
    # Get the Restaurant and SocialMedia models
    Restaurant = apps.get_model('restaurants', 'Restaurant')
    SocialMedia = apps.get_model('restaurants', 'SocialMedia')
    
    # Get the 'Sunny Bites' restaurant
    sunny_bites = Restaurant.objects.get(name="Sunny Bites")
        
    # Create SocialMedia entries with platform name and username
    SocialMedia.objects.create(
        platform_name="Instagram",
        username="sunnybites",  
        restaurant=sunny_bites
    )
    SocialMedia.objects.create(
        platform_name="Facebook",
        username="sunnybites",  
        restaurant=sunny_bites
    )
    SocialMedia.objects.create(
        platform_name="TikTok",
        username="sunnybites",  
        restaurant=sunny_bites
    )

class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_socialmedia'), 
    ]

    operations = [
        migrations.RunPython(fill_social_media),
    ]
