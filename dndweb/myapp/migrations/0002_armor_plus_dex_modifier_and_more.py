# Generated by Django 5.0.6 on 2024-05-24 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='armor',
            name='plus_dex_modifier',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='armor',
            name='plus_dex_modifier_max_2',
            field=models.BooleanField(default=False),
        ),
    ]
