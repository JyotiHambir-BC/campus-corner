# Generated by Django 4.2.16 on 2024-10-09 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_roompost_approved_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roompost',
            old_name='availiable_from',
            new_name='available_from',
        ),
        migrations.RenameField(
            model_name='roompost',
            old_name='availiable_to',
            new_name='available_to',
        ),
    ]
