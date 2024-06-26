# Generated by Django 5.0.6 on 2024-05-25 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_damagetype_weapon_damage_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('sides', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='damage',
        ),
        migrations.AddField(
            model_name='weapon',
            name='number_of_dice',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weapon',
            name='dice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.dice'),
        ),
    ]
