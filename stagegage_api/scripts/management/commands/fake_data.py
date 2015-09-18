from django.core.management.base import BaseCommand
from stagegage.tests.factories import set_up_many

class Command(BaseCommand):
    help = 'generates some test data in the database'

    def handle(self, *args, **options):
        set_up_many(10)












