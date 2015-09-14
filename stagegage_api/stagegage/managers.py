"""
Custom queries for models
"""
from django.db.models import QuerySet, Count, Sum

class ArtistQuerySet(QuerySet):

    def rank(self):
        return self.extra(select={'ranking' : """SELECT
            CASE WHEN Sum(weight) = 0 THEN 0
            ELSE Sum(weighted_score) / Sum(weight) END
            FROM stagegage_ranking WHERE stagegage_ranking.artist_id = stagegage_artist.id"""})\
            .order_by('ranking')




class GenreQuerySet(QuerySet):
    def top_genres(self, artist):
        """Return list of top 3 genres by vote."""
        return self.filter(review__artist=artist)\
                   .values_list("genre", flat=True)\
                   .annotate(votes=Count("genre"))\
                   .order_by('-votes')[:3]


class ReviewQuerySet(QuerySet):
    def latest_review(self, artist):
        """Return latest review for an artist"""
        return self.filter(artist=artist).latest("created")

