# Generated by Django 4.2.1 on 2023-05-09 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
