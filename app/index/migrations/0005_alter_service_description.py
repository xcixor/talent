# Generated by Django 4.2.1 on 2023-05-11 14:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_service_epigraph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
