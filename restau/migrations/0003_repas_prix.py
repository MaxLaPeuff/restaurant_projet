# Generated by Django 4.2.3 on 2024-02-03 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restau', '0002_rename_menu_repas'),
    ]

    operations = [
        migrations.AddField(
            model_name='repas',
            name='prix',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
