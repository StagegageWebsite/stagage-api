import factory
import random
from faker import Faker
from .models import Genre
from users.factories import UserFactory

fake = Faker()


class ArtistFactory(factory.DjangoModelFactory):

    class Meta:
        model = 'stagegage.Artist'
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'test_artist_{}'.format(n))


class FestivalFactory(factory.DjangoModelFactory):

    class Meta:
        model = 'stagegage.Festival'
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'test_festival_{}'.format(n))
    start_date = factory.lazy_attribute(lambda s: fake.date())
    ranking_set = factory.RelatedFactory(RankingSetFactory, 'festival')

    @factory.post_generation
    def artists(self, create, extraced, **kwargs):
        if not create:
            return
        if extraced:
            for artist in extraced:
                self.artists.add(artist)


class RankingSetFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'stagegage.RankingSet'

    festival = factory.SubFactory(FestivalFactory)
    user = factory.SubFactory(UserFactory)
    ranking = factory.RelatedFactory(RankingFactory, 'ranking_set')



class RankingFactory(factory.DjangoModelFactory):

    class Meta:
        model = 'stagegage.Ranking'

    score = factory.lazy_attribute(lambda s: random.uniform(0,10))
    artist = factory.SubFactory(ArtistFactory)



class GenreFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'stagegage.Genre'

    genre = factory.lazy_attribute(lambda s: random.choice([a for a,b in Genre.GENRE_CHOICES]))

class ReviewFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'stagegage.Review'


    text = factory.lazy_attribute(lambda s: fake.text())


def setup():
    pass