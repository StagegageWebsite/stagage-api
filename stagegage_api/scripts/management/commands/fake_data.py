from django.core.management.base import BaseCommand
from stagegage.factories import *
from users.factories import UserFactory
import random

class Command(BaseCommand):
    help = 'generates some test data in the database'


    def handle(self, *args, **options):
        pass












