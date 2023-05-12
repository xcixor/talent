# Generated by Django 4.2.1 on 2023-05-12 06:13

import accounts.models.user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=accounts.models.user.image_directory_path),
        ),
    ]