# Generated by Django 4.2 on 2023-04-19 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortlist', '0007_alter_application_status_alter_shortlist_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortlist',
            old_name='status',
            new_name='reviewed',
        ),
    ]