from django.db import migrations

def create_languages(apps, schema_editor):
    Language = apps.get_model('languages', 'Language')
    Language.objects.bulk_create([
        Language(code='es', name='Spanish'),
        Language(code='en', name='English'),
    ])

class Migration(migrations.Migration):
    dependencies = [
        ('languages', '0002_alter_language_code_alter_language_name'),
    ]

    operations = [
        migrations.RunPython(create_languages),
    ]