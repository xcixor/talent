# Generated by Django 4.2.1 on 2023-05-09 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_about_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='mission',
            new_name='our_mission',
        ),
    ]
