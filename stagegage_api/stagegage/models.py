from django.db import models
from users.models import User


class Artist(models.Model):
    """Defines a single artist. Has a many to many relationship with Festival."""
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300, unique=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ('name',)

class Festival(models.Model):
    """Defines a single Festival.
    start_date is date when festival starts
    Has a many to many relationship with Artist."""
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300, unique=True)
    start_date = models.DateField()
    artists = models.ManyToManyField(Artist, related_name='festivals')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ('name',)


class Ranking(models.Model):
    """Defines a numerical score for a single artist
    Associated with a single festival and user."""
    created = models.DateTimeField(auto_now_add=True)
    score = models.FloatField()
    user = models.ForeignKey(User, related_name="rankings")
    artist = models.ForeignKey(Artist, related_name='rankings')
    festival = models.ForeignKey(Festival, related_name='rankings')

    def __unicode__(self):
        return "%s : %s : %s : %f" % (self.user, self.artist, self.festival, self.score)

    class Meta:
        unique_together = ('user', 'artist', 'festival')


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
    AVANT = 'avant garde'
    BLUES = 'blues'
    COUNTRY = 'country'
    ELECTRONIC = 'electronic'
    FOLK = 'folk'
    HIPHOP = 'hip hop'
    JAZZ = 'jazz'
    POP = 'pop'
    RB = 'r&b'
    ROCK = 'rock'
    GENRE_CHOICES = [
        (AVANT, 'Avant Garde'),
        (BLUES, 'Blues'),
        (COUNTRY, 'Country'),
        (ELECTRONIC, 'Electronic'),
        (FOLK, 'Folk'),
        (HIPHOP, 'Hip Hop'),
        (JAZZ, 'Jazz'),
        (POP, 'Pop'),
        (RB, 'R&B'),
        (ROCK, 'Rock'),
    ]

    created = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    artist = models.ForeignKey(Artist, related_name='genres')
    user = models.ForeignKey(User, related_name='genres')

    def __unicode__(self):
        return self.genre




