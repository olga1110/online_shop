# Generated by Django 2.1.3 on 2018-12-26 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20181225_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='value',
            field=models.ImageField(default='product_images/default.ppg', upload_to='product_images/'),
        ),
    ]