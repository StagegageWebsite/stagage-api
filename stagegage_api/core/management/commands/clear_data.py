from django.core.management.base import BaseCommand
from stagegage.models import *
from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        Artist.objects.all().delete()
        Festival.objects.all().delete()
        User.objects.all().delete()
        RankingSet.objects.all().delete()
        Ranking.objects.all().delete()
        Genre.objects.all().delete()
        Review.objects.all().delete()

