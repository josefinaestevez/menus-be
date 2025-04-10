# Generated by Django 5.1.5 on 2025-04-08 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_add_sunny_bites_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(choices=[('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('TikTok', 'TikTok'), ('Twitter', 'Twitter')], max_length=50)),
                ('username', models.CharField(max_length=255)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media', to='restaurants.restaurant')),
            ],
        ),
    ]
