# Generated by Django 2.1.1 on 2018-10-13 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_product_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['price', 'modified', 'created']},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='active',
            new_name='is_active',
        ),
    ]