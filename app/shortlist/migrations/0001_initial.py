# Generated by Django 4.1.9 on 2023-05-25 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('in_review', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('UNASSIGNED', 'UNASSIGNED'), ('IN_PROGRESS', 'IN_PROGRESS'), ('ACCEPTED', 'ACCEPTED'), ('DECLINED', 'DECLINED'), ('COMPLETED', 'COMPLETED')], default='UNASSIGNED', max_length=40)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='job.joblisting')),
            ],
            options={
                'ordering': ['created'],
                'unique_together': {('applicant', 'listing')},
            },
        ),
        migrations.CreateModel(
            name='ShortList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_reviewed', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shortlisters', to='shortlist.application')),
                ('shortlister', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shortlists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
                'unique_together': {('application', 'shortlister')},
            },
        ),
    ]
