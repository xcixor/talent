# Generated by Django 4.1.9 on 2024-04-11 03:40

import accounts.models.user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_joined', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_of_birth', models.DateField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=accounts.models.user.image_directory_path)),
                ('resume', models.FileField(blank=True, max_length=400, null=True, upload_to=accounts.models.user.image_directory_path)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('years_of_work', models.IntegerField(blank=True, null=True)),
                ('country_code', models.CharField(blank=True, max_length=255, null=True)),
                ('preferred_country', models.CharField(blank=True, max_length=255, null=True)),
                ('service_type', models.CharField(blank=True, max_length=255, null=True)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('country_of_residence', models.CharField(blank=True, max_length=255, null=True)),
                ('highest_level_of_education', models.CharField(blank=True, max_length=255, null=True)),
                ('type_of_visa', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_url', models.URLField(blank=True, max_length=255, null=True)),
                ('mode_of_contact', models.CharField(blank=True, max_length=255, null=True)),
                ('type_of_user', models.CharField(choices=[('ADMIN', 'Admin'), ('STAFF', 'Staff'), ('EMPLOYER', 'Employer'), ('JOB_SEEKER', 'Job Seeker')], max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['date_joined'],
            },
        ),
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=400)),
                ('tax_number', models.IntegerField(blank=True, null=True)),
                ('address_line_one', models.CharField(blank=True, max_length=400, null=True)),
                ('address_line_two', models.CharField(blank=True, max_length=400, null=True)),
                ('city', models.CharField(blank=True, max_length=400, null=True)),
                ('state', models.CharField(blank=True, max_length=400, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=400, null=True)),
                ('country', models.CharField(blank=True, max_length=400, null=True)),
                ('company_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Company Details',
            },
        ),
    ]
