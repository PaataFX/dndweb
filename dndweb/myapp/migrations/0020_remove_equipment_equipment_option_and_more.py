# Generated by Django 5.0.6 on 2024-05-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_item_cost_alter_item_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='equipment_option',
        ),
        migrations.AddField(
            model_name='equipment',
            name='ArmorGroup',
            field=models.ManyToManyField(blank=True, related_name='equipments', to='myapp.armorgroup'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='WeaponGroup',
            field=models.ManyToManyField(blank=True, related_name='equipments', to='myapp.weapongroup'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='armors',
            field=models.ManyToManyField(blank=True, related_name='equipments', to='myapp.armor'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_options',
            field=models.ManyToManyField(blank=True, related_name='equipments', to='myapp.equipmentoption'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='tools',
            field=models.ManyToManyField(blank=True, related_name='equipments', to='myapp.tool'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='weapons',
            field=models.ManyToManyField(blank=True, related_name='equipments', to='myapp.weapon'),
        ),
    ]
