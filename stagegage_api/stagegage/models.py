"""Database models for all objects related to Ranking.

models in the file:
    Artist
    Festival
    Performance
    RankingSet
    Ranking
    Review
    Genre
"""

from django.conf import settings
from django.db import models
from django.utils import timezone
from model_utils.managers import PassThroughManager
from stagegage.managers import ReviewQuerySet
from stagegage.managers import GenreQuerySet
from users.models import User

class Artist(models.Model):
    """An Artist or Band that plays at a festival

    Attributes:
        created: Date and time when object is created, set automatically
        name: Name of artist
        score: Overall score for the artist from all rankings.
    						 This is a calculated score that is run as a cron job.
    						 See scripts/../../score.py for more info
    	Has a many to many relationship with festivals through the Performance model.
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300, unique=True)
    score = models.FloatField(default=0, editable=False)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ('name',)


class Festival(models.Model):
    """Festival or concert that artists play at.

    Attributes:
        created: when model object is created
        name: Name of festival
        start_date: date when festival starts
    			performances: The artists and other data that play at the festival

    Has a many to many relationship with Artist through the Performance model.
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300, unique=True)
    start_date = models.DateField()
    performances = models.ManyToManyField(Artist, through="Performance")

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ('name',)


class Performance(models.Model):
    """An artists that performs at a festival along with its score.

    Attributes:
    created: When the modle object was created.
    artist: The artists that is performing.
    festival: The festival where the artist plays.
    score: The average score of the artist at that festival.
    	 notice this is different from the overall artist score attirbute.
    """
    created = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist)
    festival = models.ForeignKey(Festival)
    score = models.FloatField(default=0, editable=False)


class RankingSet(models.Model):
    """A group of rankings submitted by a user at once.

    This is mostly used to group a set of rankings together with a single user.
    Attributes:
    		created: When the model object as created.
    		user: The user that created the rankings
    		festival: The festival the user is ranking.
    """
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="ranking_sets")
    festival = models.ForeignKey(Festival, related_name='ranking_sets')

    def __unicode__(self):
        return "{} : {}".format(self.user, self.festival)

    class Meta:
        unique_together = ('user', 'festival')



class Ranking(models.Model):
    """A single numerical ranking for an Artist at a Festival.

    	Attributes:
    			ranking_set: The group of rankings this ranking is part of
    			score: The numerical score of the artist.
    			artist: The artist the user is ranking.
    """
    ranking_set = models.ForeignKey(RankingSet, related_name="rankings")
    score = models.FloatField()
    artist = models.ForeignKey(Artist, related_name="rankings")


    def __unicode__(self):
        return "{} : {}".format(self.artist, self.score)



class Review(models.Model):
    """A text based review of an artist at a festival.

    	Does not affect the numerical score of an artist or Performance
    	Attributes:
    			created: When the model object was created.
    			text: The text of the review.
    			user: The user writing the review
    			artist: The artist being reviewed
    			festival: The festival where the artist is playing
    			objects: A custom Query Manager. See managers.py for more detail.
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
    """A user generated genre for an artist that is part of an artist review.

    Attributes:
    		created: When the model object was created.
    		genre: The user choice of genre, chosen from GENRE_CHOICES
    		review: The review the genre choice is associated with
    		objects: A custom Query manager. See managers.py for more detail.
    """
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


