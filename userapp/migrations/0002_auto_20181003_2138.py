# Generated by Django 2.1.1 on 2018-10-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuser',
            name='age',
        ),
        migrations.AddField(
            model_name='shopuser',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
