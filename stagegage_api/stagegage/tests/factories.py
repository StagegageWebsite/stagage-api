import random

import factory
from faker import Faker
from stagegage.models import Genre
from users.tests.factories import UserFactory


fake = Faker()


class ArtistFactory(factory.DjangoModelFactory):

    class Meta:
        model = 'stagegage.Artist'
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'test_artist_{}'.format(n))
    score = factory.lazy_attribute(lambda s: round(random.uniform(0, 10), 5))




class FestivalFactory(factory.DjangoModelFactory):

    class Meta:
        model = 'stagegage.Festival'
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'test_festival_{}'.format(n))
    start_date = factory.lazy_attribute(lambda s: fake.date())

    @factory.post_generation
    def artists(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of artists were passed in, use them
            for artist in extracted:
                self.artists.add(artist)


class RankingSetFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'stagegage.RankingSet'

    festival = factory.SubFactory(FestivalFactory)
    user = factory.SubFactory(UserFactory)



class RankingFactory(factory.DjangoModelFactory):

    class Meta:
        model = 'stagegage.Ranking'

    score = factory.lazy_attribute(lambda s: random.uniform(0,10))
    ranking_set = factory.SubFactory(RankingSetFactory)
    artist = factory.SubFactory(ArtistFactory)


class ReviewFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'stagegage.Review'

    text = factory.lazy_attribute(lambda s: fake.text())
    user = factory.SubFactory(UserFactory)
    artist = factory.SubFactory(ArtistFactory)
    festival = factory.SubFactory(FestivalFactory)


class GenreFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'stagegage.Genre'

    genre = factory.lazy_attribute(lambda s: random.choice([a for a,b in Genre.GENRE_CHOICES]))
    review = factory.SubFactory(ReviewFactory)


def set_up_single():
    """Set up a single instance of each model."""
    #TODO: admin factory
    user = UserFactory(username='admin', is_staff=True)
    artist = ArtistFactory()
    festival = FestivalFactory(artists=(artist,))
    ranking_set = RankingSetFactory(festival=festival, user=user)
    ranking = RankingFactory(ranking_set=ranking_set, artist=artist)
    review = ReviewFactory(user=user, artist=artist, festival=festival)
    genre = GenreFactory(review=review)
    return {'user': user,
            'artist': artist,
            'festival': festival,
            'ranking_set': ranking_set,
            'ranking': ranking,
            'genre': genre,
            'review': review}

def set_up_many(num_instances):
    """Set up many instances."""
    users = UserFactory.create_batch(num_instances)
    artists = ArtistFactory.create_batch(num_instances)
    festivals = FestivalFactory.create_batch(num_instances, artists=artists)
    ranking_sets = []
    rankings = []
    reviews = []
    genres = []
    for user in users:
        for festival in festivals:
            ranking_set = RankingSetFactory.create(festival=festival, user=user)
            ranking_sets.append(ranking_set)
            for artist in artists:
                ranking = RankingFactory.create(ranking_set=ranking_set, artist=artist)
                rankings.append(ranking)

                review = ReviewFactory.create(user=user, artist=artist, festival=festival)
                reviews.append(review)

                genre = GenreFactory.create(review=review)
                genres.append(genre)
    return {'users': users,
            'artists': artists,
            'festivals': festivals,
            'ranking_sets': ranking_sets,
            'rankings': rankings,
            'reviews': reviews,
            'genres': genres}


