# Generated by Django 5.0.6 on 2024-06-07 16:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.PositiveIntegerField(default=1)),
                ('experience_points', models.PositiveIntegerField(default=0)),
                ('hit_points', models.PositiveIntegerField()),
                ('max_hit_points', models.PositiveIntegerField()),
                ('temporary_hit_points', models.PositiveIntegerField(default=0)),
                ('armor_class', models.PositiveIntegerField()),
                ('initiative', models.IntegerField()),
                ('speed', models.PositiveIntegerField()),
                ('alignment', models.CharField(max_length=50)),
                ('background', models.CharField(max_length=100)),
                ('proficiency_bonus', models.IntegerField()),
                ('strength', models.PositiveIntegerField()),
                ('dexterity', models.PositiveIntegerField()),
                ('constitution', models.PositiveIntegerField()),
                ('intelligence', models.PositiveIntegerField()),
                ('wisdom', models.PositiveIntegerField()),
                ('charisma', models.PositiveIntegerField()),
                ('actions', models.TextField(blank=True)),
                ('dnd_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.class')),
                ('equipment', models.ManyToManyField(to='myapp.equipment')),
                ('features', models.ManyToManyField(to='myapp.trait')),
                ('languages', models.ManyToManyField(to='myapp.language')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to=settings.AUTH_USER_MODEL)),
                ('proficiencies', models.ManyToManyField(to='myapp.proficiency')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.race')),
                ('saving_throws', models.ManyToManyField(to='myapp.savingthrow')),
                ('skills', models.ManyToManyField(to='myapp.skill')),
                ('spells', models.ManyToManyField(to='myapp.spell')),
                ('subclass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.subclass')),
                ('subrace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.subrace')),
            ],
        ),
    ]
