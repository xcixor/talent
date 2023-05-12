import os
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from accounts.models import User


class Command(BaseCommand):
    help = ('Automatically creates a Super user')

    def handle(self, *args, **options):
        try:
            # USER ONE
            UserModel = get_user_model()
            job_seeker_one_email = os.getenv('JOB_SEEKER_ONE_EMAIL')
            job_seeker_one_password = os.getenv('JOB_SEEKER_ONE_PASSWORD')
            success_message = 'Job Seeker One created.'
            extra_fields = {
                'first_name': 'Ali',
                'last_name': 'Hassan',
                'type_of_user': 'JOB_SEEKER',
                'nationality': 'Kenya',
                'service_type': 'Food and Beverage',
                'preferred_country': 'Qatar',
                'pk': 2
            }
            if not User.objects.filter(email=job_seeker_one_email).first():
                UserModel.objects._create_user(
                    job_seeker_one_email, job_seeker_one_password, **extra_fields)
                self.stdout.write(self.style.SUCCESS(success_message))
            else:
                warning_msg = f"{job_seeker_one_email} already exists."
                self.stdout.write(self.style.WARNING(warning_msg))

            # USER THREE
            job_seeker_two_email = os.getenv('JOB_SEEKER_TWO_EMAIL')
            job_seeker_two_password = os.getenv('JOB_SEEKER_TWO_PASSWORD')
            success_message = 'Job Seeker Two created.'
            extra_fields = {
                'first_name': 'Omari',
                'last_name': 'Kajembe',
                'type_of_user': 'JOB_SEEKER',
                'nationality': 'Tanzania',
                'service_type': 'Food and Beverage',
                'preferred_country': 'Kuwait',
                'pk': 3

            }
            if not User.objects.filter(email=job_seeker_two_email).first():
                UserModel.objects._create_user(
                    job_seeker_two_email, job_seeker_two_password, **extra_fields)
                self.stdout.write(self.style.SUCCESS(success_message))
            else:
                warning_msg = f"{job_seeker_two_email} already exists."
                self.stdout.write(self.style.WARNING(warning_msg))

            # USER THREE
            job_seeker_three_email = os.getenv('JOB_SEEKER_THREE_EMAIL')
            job_seeker_three_password = os.getenv('JOB_SEEKER_THREE_PASSWORD')
            success_message = 'Job Seeker Three created.'
            extra_fields = {
                'first_name': 'Nancy',
                'last_name': 'Waringa',
                'type_of_user': 'JOB_SEEKER',
                'nationality': 'Kenya',
                'service_type': 'Sales and Marketing',
                'preferred_country': 'Australia',
                'pk': 4
            }
            if not User.objects.filter(email=job_seeker_three_email).first():
                UserModel.objects._create_user(
                    job_seeker_three_email, job_seeker_three_password, **extra_fields)
                self.stdout.write(self.style.SUCCESS(success_message))
            else:
                warning_msg = f"{job_seeker_three_email} already exists."
                self.stdout.write(self.style.WARNING(warning_msg))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
            raise CommandError("Error creating job seeker one")
