# Generated by Django 4.2 on 2023-04-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlist', '0004_shortlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='in_review',
            field=models.BooleanField(default=False),
        ),
    ]
