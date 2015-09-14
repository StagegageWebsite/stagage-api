from django.db import models
from django.utils import timezone
from model_utils.managers import PassThroughManager
from users.models import User
from .managers import ReviewQuerySet, GenreQuerySet, ArtistQuerySet


class Artist(models.Model):
    """Defines a single artist. Has a many to many relationship with Festival."""
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300, unique=True)
    objects = PassThroughManager.for_queryset_class(ArtistQuerySet)()

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ('name',)


class Festival(models.Model):
    """
    Defines a single Festival.
    start_date is date when festival starts
    Has a many to many relationship with Artist.
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300, unique=True)
    start_date = models.DateField()
    artists = models.ManyToManyField(Artist, related_name='festivals')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ('name',)


class RankingSet(models.Model):
    """Defines a group of rankings for a festival by a user."""
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="ranking_sets")
    festival = models.ForeignKey(Festival, related_name='ranking_sets')

    def set_weight(self):
        """Set weight of ranking set and all rankings."""
        ranking_weight = 0
        num_rankings = self.rankings.count()
        if num_rankings > 4:
            # If first ranking set by user weight is 0.5
            # If second ranking set weight is 0.75
            list_of_rs = list(self.user.ranking_sets.all())
            index = list_of_rs.index(self)
            if index == 1:
                weight_by_order = 0.5
            elif index == 2:
                weight_by_order = 0.75
            else:
                weight_by_order = 1

            # Every six months decrease weight by 0.1 until 0.6
            delta = timezone.now() - self.created

            # using 30 days as a proxy for one month
            delta_months = delta.days / 30
            num_six_months = delta_months / 6

            # if more than 2 years old set weight to 0.6
            if num_six_months > 3:
                weight_by_time =.6
            else:
                weight_by_time = 1 - (0.1 * num_six_months)

            ranking_weight = weight_by_order * weight_by_time

        # Now set weighted ranking of each ranking
        for ranking in self.rankings.all():
            ranking.weight = ranking_weight
            ranking.weighted_score = ranking.score * ranking_weight


    def __unicode__(self):
        return "{} : {}".format(self.user, self.festival)

    class Meta:
        unique_together = ('user', 'festival')



class Ranking(models.Model):
    """
    Defines a numerical score for a single artist
    Associated with a single festival and user.
    """
    ranking_set = models.ForeignKey(RankingSet, related_name="rankings")
    score = models.FloatField()
    artist = models.ForeignKey(Artist, related_name="rankings")
    weight = models.FloatField(default=0)
    weighted_score = models.FloatField(default=0)


    def __unicode__(self):
        return "{} : {}".format(self.artist, self.score)



class Review(models.Model):
    """
    Defines a text review of a single artist
    Associated with a single festival and user.
    """
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    user = models.ForeignKey(User, related_name='reviews')
    artist = models.ForeignKey(Artist, related_name='reviews')
    festival = models.ForeignKey(Festival, related_name='reviews')
    objects = PassThroughManager.for_queryset_class(ReviewQuerySet)()

    def __unicode__(self):
        return unicode(self.text[:100])

    class Meta:
        unique_together = ('user', 'artist', 'festival')


class Genre(models.Model):
    """Defines a choice of genre for an artist."""
    GENRE_CHOICES = [
        ('avant garde', 'Avant Garde'),
        ('blues', 'Blues'),
        ('country', 'Country'),
        ('electronic', 'Electronic'),
        ('folk', 'Folk'),
        ('hip hop', 'Hip Hop'),
        ('jazz', 'Jazz'),
        ('pop', 'Pop'),
        ('r&b', 'R&B'),
        ('rock', 'Rock'),
    ]

    created = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    review = models.ForeignKey(Review, related_name='genres')
    objects = PassThroughManager.for_queryset_class(GenreQuerySet)()

    def __unicode__(self):
        return self.genre




