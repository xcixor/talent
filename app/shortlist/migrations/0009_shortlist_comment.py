# Generated by Django 4.2 on 2023-04-19 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlist', '0008_rename_status_shortlist_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortlist',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
