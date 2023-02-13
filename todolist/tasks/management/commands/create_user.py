
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create new regular user'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            action='store',
        )

    def handle(self, *args, **options):
        username = options['username']
        mail = input('Enter mail: ')
        password = input('Enter password: ')
        User.objects.create_user(username, mail, password)



