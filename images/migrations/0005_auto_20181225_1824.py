# Generated by Django 2.1.3 on 2018-12-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20181225_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='value',
            field=models.ImageField(default='product_images/default.png', upload_to='product_images/'),
        ),
    ]
