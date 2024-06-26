# Generated by Django 5.0.6 on 2024-06-08 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_alter_character_armor_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='alignment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='background',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='equipment',
            field=models.ManyToManyField(blank=True, to='myapp.equipment'),
        ),
        migrations.AlterField(
            model_name='character',
            name='features',
            field=models.ManyToManyField(blank=True, to='myapp.trait'),
        ),
        migrations.AlterField(
            model_name='character',
            name='hit_points',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='initiative',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='languages',
            field=models.ManyToManyField(blank=True, to='myapp.language'),
        ),
        migrations.AlterField(
            model_name='character',
            name='max_hit_points',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='character',
            name='proficiencies',
            field=models.ManyToManyField(blank=True, to='myapp.proficiency'),
        ),
        migrations.AlterField(
            model_name='character',
            name='proficiency_bonus',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='character',
            name='saving_throws',
            field=models.ManyToManyField(blank=True, to='myapp.savingthrow'),
        ),
        migrations.AlterField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(blank=True, to='myapp.skill'),
        ),
        migrations.AlterField(
            model_name='character',
            name='speed',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='character',
            name='spells',
            field=models.ManyToManyField(blank=True, to='myapp.spell'),
        ),
    ]
