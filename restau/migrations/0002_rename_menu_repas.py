# Generated by Django 4.2.3 on 2024-02-03 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restau', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='Repas',
        ),
    ]