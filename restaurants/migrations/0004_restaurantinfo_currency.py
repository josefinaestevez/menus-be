# Generated by Django 5.1.5 on 2025-04-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_add_example_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantinfo',
            name='currency',
            field=models.CharField(default='EUR', max_length=3),
        ),
    ]
