from django.core.management.base import BaseCommand
from django.utils import timezone
from stagegage.models import RankingSet, Artist


class Command(BaseCommand):
    def handle(self, *args, **options):
        artist_weights = {}

        # Iterate through all ranking sets
        all_ranking_sets = RankingSet.objects.all()
        for ranking_set in all_ranking_sets:
            #If ranking set has less than 4 rankings, ignore it
            num_rankings = ranking_set.rankings.count()
            if num_rankings > 4:
                # If first ranking set by user weight is 0.5
                # If second ranking set weight is 0.75
                index = list(ranking_set.user.ranking_sets.all()).index(ranking_set)
                if index == 0:
                    weight_by_order = 0.5
                elif index == 1:
                    weight_by_order = 0.75
                else:
                    weight_by_order = 1

                # Every six months decrease weight by 0.1 until 0.6
                delta = timezone.now() - ranking_set.created

                # using 30 days as a proxy for one month
                delta_months = delta.days / 30
                num_six_months = delta_months / 6

                # if more than 2 years old set weight to 0.6
                if num_six_months > 3:
                    weight_by_time = 0.6
                else:
                    weight_by_time = 1 - (0.1 * num_six_months)

                ranking_weight = weight_by_order * weight_by_time

                for ranking in ranking_set.rankings.all():
                    weighted_score = ranking.score
                    scores, weights = artist_weights.get(ranking.artist.id, ([],[]))
                    scores.append(weighted_score)
                    weights.append(ranking_weight)
                    artist_weights[ranking.artist.id] = (scores, weights)

        for artist in Artist.objects.all():
            scores, weights = artist_weights[artist.id]
            if weights:
                artist.score = sum(scores) / sum(weights)
                artist.save()

