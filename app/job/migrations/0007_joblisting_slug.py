# Generated by Django 4.2 on 2023-04-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_joblisting_options_joblisting_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='slug',
            field=models.SlugField(
                help_text='Unique address for the opening.', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
