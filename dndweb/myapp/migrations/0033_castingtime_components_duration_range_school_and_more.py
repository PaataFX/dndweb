# Generated by Django 5.0.6 on 2024-06-08 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_alter_character_alignment_alter_character_background_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CastingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='spell',
            name='casting_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.castingtime'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='components',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.components'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='duration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.duration'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='range',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.range'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.school'),
        ),
    ]
