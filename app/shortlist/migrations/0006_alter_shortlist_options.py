# Generated by Django 4.2 on 2023-04-19 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortlist', '0005_application_in_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortlist',
            options={'ordering': ['created']},
        ),
    ]
