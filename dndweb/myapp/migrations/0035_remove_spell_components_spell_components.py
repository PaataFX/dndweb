# Generated by Django 5.0.6 on 2024-06-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_spell_damage_type_spell_dice_spell_dice_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spell',
            name='components',
        ),
        migrations.AddField(
            model_name='spell',
            name='components',
            field=models.ManyToManyField(to='myapp.components'),
        ),
    ]
