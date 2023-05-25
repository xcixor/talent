# Generated by Django 4.1.9 on 2023-05-25 08:22

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import index.models.services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('subtitle', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('epigraph', models.TextField()),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(upload_to=index.models.services.image_directory_path)),
                ('slug', models.SlugField(help_text='Unique verbose identifier for the service.', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('link', models.URLField()),
                ('is_outlined', models.BooleanField(default=False)),
                ('carousel_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='index.carouselitem')),
            ],
        ),
    ]
