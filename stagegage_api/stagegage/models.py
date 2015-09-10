from django.db import models
from django.utils import timezone
from users.models import User


class Artist(models.Model):
    """
    Defines a single artist. Has a many to many relationship with Festival.
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300, unique=True)

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
    """
    Defines a group of rankings by a user
    """
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="ranking_set")
    festival = models.ForeignKey(Festival, related_name='ranking_set')


    class Meta:
        unique_together = ('user', 'festival')



class Ranking(models.Model):
    """Defines a numerical score for a single artist
    Associated with a single festival and user."""
    ranking_set = models.ForeignKey(RankingSet, related_name="rankings")
    score = models.FloatField()
    artist = models.ForeignKey(Artist)



class Review(models.Model):
    """Defines a text review of a single artist
    Associated with a single festival and user."""
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    user = models.ForeignKey(User, related_name='reviews')
    artist = models.ForeignKey(Artist, related_name='reviews')
    festival = models.ForeignKey(Festival, related_name='reviews')

    def __unicode__(self):
        return self.text[:100]

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
    artist = models.ForeignKey(Artist, related_name='genres')
    user = models.ForeignKey(User, related_name='genres')

    def __unicode__(self):
        return self.genre




