# Generated by Django 5.0.6 on 2024-06-08 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='armor_class',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
