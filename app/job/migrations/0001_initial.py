# Generated by Django 4.1.9 on 2023-05-25 07:43

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
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(help_text='Unique address for the industry.', max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Job Categories',
            },
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('requirements', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('length_of_hire', models.CharField(blank=True, max_length=200, null=True)),
                ('proposed_remuneration', models.CharField(blank=True, max_length=400, null=True)),
                ('cooperation_type', models.CharField(blank=True, max_length=400, null=True)),
                ('openings', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('slug', models.SlugField(help_text='Unique address for the opening.', max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('experience', ckeditor.fields.RichTextField(blank=True, max_length=200, null=True)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='openings', to='job.industry')),
                ('job_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Job Listing',
                'ordering': ['industry'],
                'unique_together': {('job_owner', 'title', 'city')},
            },
        ),
    ]
