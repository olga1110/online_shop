# Generated by Django 2.1.1 on 2018-09-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование продукта')),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('short_desc', models.CharField(blank=True, max_length=60, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, verbose_name='Подробное описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Скидка')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество на складе')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
