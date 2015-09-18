"""
Custom queries for models
"""
from django.db.models import QuerySet, Count

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
        qs = self.filter(artist=artist)
        if qs.exists():
            qs = qs.latest("created")
        return qs


