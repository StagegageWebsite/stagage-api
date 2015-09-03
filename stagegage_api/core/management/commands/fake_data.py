from django.core.management.base import BaseCommand
from stagegage.factories import *
from users.factories import UserFactory
import random

class Command(BaseCommand):
    help = 'generates some test data in the database'

    NUM_ARTISTS = 100
    NUM_FESTIVALS = 5
    NUM_ARTISTS_PER_FEST = 50
    NUM_USERS = 10
    NUM_RANKING_SETS = NUM_USERS * NUM_FESTIVALS
    NUM_RANKINGS = NUM_RANKING_SETS * NUM_ARTISTS_PER_FEST
    NUM_GENRES_PER_ARTIST = 10
    NUM_GENRES = NUM_GENRES_PER_ARTIST * NUM_ARTISTS * NUM_USERS
    NUM_REVIEWS = NUM_USERS * NUM_ARTISTS * NUM_FESTIVALS

    def handle(self, *args, **options):

        # create artists
        artists = ArtistFactory.create_batch(size=self.NUM_ARTISTS)

        # create festivals
        festivals = FestivalFactory.create_batch(size=self.NUM_FESTIVALS)
        for festival in festivals:
            festival.artists.add(*random.sample(artists, self.NUM_ARTISTS_PER_FEST))

        #create users
        users = UserFactory.create_batch(size=self.NUM_USERS)

        # create ranking sets
        ranking_sets = RankingSetFactory.build_batch(size=self.NUM_RANKING_SETS)
        for i, user in enumerate(users):
            for j, festival in enumerate(festivals):
                index = i * self.NUM_FESTIVALS + j
                ranking_set = ranking_sets[index]
                ranking_set.user = user
                ranking_set.festival = festival
                ranking_set.save()

        # create rankings
        rankings = RankingFactory.build_batch(size=self.NUM_RANKINGS)
        for i, ranking_set in enumerate(ranking_sets):
            festival = ranking_set.festival
            for j, artist in enumerate(festival.artists.all()):
                index = i * self.NUM_ARTISTS_PER_FEST + j
                ranking = rankings[index]
                ranking.artist = artist
                ranking.ranking_set = ranking_set
                ranking.save()

        # create Genres
        genres = GenreFactory.build_batch(size=self.NUM_GENRES)
        for i, user in enumerate(users):
            for j, artist in enumerate(artists):
                for k in xrange(self.NUM_GENRES_PER_ARTIST):
                    index = i * self.NUM_ARTISTS + j * self.NUM_GENRES_PER_ARTIST + k
                    genre = genres[index]
                    genre.artist = artist
                    genre.user = user
                    genre.save()

        # create Reviews
        reviews = ReviewFactory.build_batch(size=self.NUM_REVIEWS)
        for i, user in enumerate(users):
            for j, artist in enumerate(artists):
                for k, fest in enumerate(festivals):
                    index = i * self.NUM_ARTISTS + j * self.NUM_FESTIVALS + k
                    review = reviews[index]
                    review.user = user
                    review.artist = artist
                    review.festival = fest
                    review.save()













