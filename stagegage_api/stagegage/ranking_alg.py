"""
Ranking algorithm
Each ranking set loses .1 every six months until .6
the first ranking set for a user gets .5, the second .75
only inlucde ranking sets with more than 3 rankings
"""
from stagegage.models import RankingSet, Ranking
from django.utils import timezone
from django.db.models import Count
from numpy import average as np_average
from collections import defaultdict


class RankingAlgorithm:
    """
    Runs the ranking algorithm for either all bands or a specific festival
    then can ask for the position of a specific band
    """
    MIN_RANKINGS = 3


    def __init__(self, festival=None):
        """ Runs main algorithm on init """

        # A dict to a list of tuples {'name' : [(a,b)]}
        artist_weights = defaultdict(list)

        # Get all rankings ordered by user and ranking set
        rankings_qs = Ranking.objects.all()\
            .values('id', 'score', 'artist', 'ranking_set', 'ranking_set__created', 'ranking_set__user')\
            .order_by('ranking_set__user', 'ranking_set')

        if festival:
            rankings_qs = rankings_qs.filter(ranking_set__festival=festival)

        # Get set of all ranking sets with less than min number of rankings
        zero_weight_ranking_sets = set(RankingSet.objects.
                                       annotate(num_rankings=Count('rankings')).
                                       filter(num_rankings__lt=self.MIN_RANKINGS).
                                       values_list('id', flat=True))

        # Initialize user and ranking set
        user = rankings_qs[0]['ranking_set__user']
        ranking_set = rankings_qs[0]['ranking_set']
        ranking_set_count = 1

        # Iterate through query set and build artist weights
        for entry in rankings_qs:
            #if new user than reset ranking set and count
            if entry['ranking_set__user'] != user:
                ranking_set = entry['ranking_set']
                ranking_set_count = 1

            #if new ranking set increment count
            if entry['ranking_set'] != ranking_set:
                ranking_set = entry['ranking_set']
                ranking_set_count += 1

            # Don't include ranking sets with less than min rankings
            if entry['ranking_set'] not in zero_weight_ranking_sets:
                # Calculate ranking weight
                order_weight = self._weight_by_order(ranking_set_count)
                time_weight = self._weight_by_time(entry['ranking_set__created'])
                total_weight = order_weight * time_weight

                # Default dict will automatically create list
                artist_weights[entry['artist']].append((entry['score'], total_weight))

        # average out weights into a list
        artist_ranks = []
        for artist in artist_weights.keys():
            scores, weights = zip(*artist_weights[artist])
            artist_ranks.append((artist, np_average(scores, weights=weights)))

        # sort artists by rank
        artist_ranks.sort(key=lambda (a,b): b)

        #create dictionary of artist to order
        self.rankings = dict(enumerate_tuple(artist_ranks))


    def get_rank(self, artist):
        return self.rankings[artist]


    ###########################
    #Private helper methods
    ###########################
    def _weight_by_order(self, count):
        """
        If first ranking set weight = 0.5
        If second ranking set weight = 0.75
        Otherwise weight is 1
        """
        if count == 1:
            return 0.5
        elif count == 2:
            return 0.75
        return 1


    def _weight_by_time(self, date):
        """
        The ranking loses .1 weight every six months, capped at .6
        """
        delta = timezone.now() - date

        # using 30 days as a proxy for one month
        months_since = delta.days / 30
        six_months_increments = months_since / 6

        # if more than 2 years old
        if six_months_increments > 3:
            return .6

        return 1 - (.1 * six_months_increments)

def enumerate_tuple(lst):
    """enumerate a list of tuple
    generate (first element of tuple, index)
    """
    i = 1
    for a,b in lst:
        yield (a, i)
        i += 1





