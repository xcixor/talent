import os
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from accounts.models import User


class Command(BaseCommand):
    help = ('Automatically creates a Super user')

    def handle(self, *args, **options):
        try:
            UserModel = get_user_model()
            email = os.getenv('ADMIN_EMAIL')
            first_name = os.getenv('ADMIN_FIRST_NAME')
            last_name = os.getenv('ADMIN_LAST_NAME')
            type_of_user = 'ADMIN'
            password = os.getenv('ADMIN_PASSWORD')
            success_message = 'Super User created.'
            extra_fields = {
                'first_name': first_name,
                'last_name': last_name,
                'type_of_user': type_of_user
            }
            if not User.objects.filter(email=email).first():
                UserModel.objects.create_superuser(
                    email, password, **extra_fields)
                self.stdout.write(self.style.SUCCESS(success_message))
            else:
                warning_msg = "That user already exists."
                self.stdout.write(self.style.WARNING(warning_msg))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
            raise CommandError("Error creating super user")
