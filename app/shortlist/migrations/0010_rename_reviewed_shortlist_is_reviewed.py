# Generated by Django 4.2 on 2023-04-19 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortlist', '0009_shortlist_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortlist',
            old_name='reviewed',
            new_name='is_reviewed',
        ),
    ]