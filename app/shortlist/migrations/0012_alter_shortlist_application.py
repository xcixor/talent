# Generated by Django 4.2 on 2023-04-19 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortlist', '0011_alter_application_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlist',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shortlisters', to='shortlist.application'),
        ),
    ]
