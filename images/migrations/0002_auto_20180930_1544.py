# Generated by Django 2.1.1 on 2018-09-30 10:44

from django.db import migrations

def create_default_image(apps, schema_editor):
    Image=apps.get_model('images', 'Image')
    Image.objects.create(
        name='table',
        value='table.jpg'
    )




class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_default_image,
            lambda x,y: (x,y)
        )
    ]
