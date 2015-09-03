import factory
import random
from faker import Faker
from .models import Genre

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



class RankingFactory(factory.DjangoModelFactory):

    class Meta:
        model = 'stagegage.Ranking'

    score = factory.lazy_attribute(lambda s: random.uniform(0,10))



class GenreFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'stagegage.Genre'

    genre = factory.lazy_attribute(lambda s: random.choice([a for a,b in Genre.GENRE_CHOICES]))

class ReviewFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'stagegage.Review'


    text = factory.lazy_attribute(lambda s: fake.text())