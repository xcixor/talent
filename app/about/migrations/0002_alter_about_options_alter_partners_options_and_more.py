# Generated by Django 4.2.1 on 2023-05-09 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About Us Content'},
        ),
        migrations.AlterModelOptions(
            name='partners',
            options={'verbose_name_plural': 'Partners'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name_plural': 'Staff'},
        ),
        migrations.AlterModelOptions(
            name='values',
            options={'verbose_name_plural': 'Values'},
        ),
        migrations.RenameField(
            model_name='values',
            old_name='cicon',
            new_name='icon',
        ),
    ]
