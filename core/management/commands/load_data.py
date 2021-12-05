from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load Courses and Modules'

    def handle(self, *args, **kwargs):
        raise NotImplementedError