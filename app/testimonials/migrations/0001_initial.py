# Generated by Django 4.1.9 on 2024-04-11 03:40

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimony', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(help_text='Unique address for the testimony.', max_length=255, unique=True)),
                ('witness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Testimonies',
            },
        ),
        migrations.CreateModel(
            name='BestTestimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimony', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='best', to='testimonials.testimony')),
            ],
        ),
    ]
