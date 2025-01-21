from django.core.management.base import BaseCommand
from myoil.models import CustomUser
from django.core.management import call_command
import os
from dotenv import load_dotenv

load_dotenv()

class Command(BaseCommand):
    help = 'Create superuser automatically'

    def handle(self, *args, **kwargs):
        username = os.environ.get('username')
        password = os.environ.get('password')
        email = os.environ.get('email')

        if not CustomUser.objects.filter(username=username).exists():  # CustomUser modelidan foydalaning
            CustomUser.objects.create_superuser(username=username, password=password, email=email)
            self.stdout.write(self.style.SUCCESS('Superuser successfully created'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
