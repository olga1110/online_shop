# Generated by Django 2.1.1 on 2018-09-30 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_category_short_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='images.Image'),
        ),
    ]
