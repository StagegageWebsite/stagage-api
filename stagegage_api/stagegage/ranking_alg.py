"""
Ranking algorithm
"""

class RankingAlg:
    MIN_NUM_RANKINGS = 3


    def __init__(self, artist):
        self.artist = artist

    def ranking(self):
        return 5

    def min_num_rankings(self):
        pass
        # RankingSet.objects.annotate(num_rankings=Count('rankings')).filter(num_rankings__gte=self.MIN_NUM_RANKINGS)