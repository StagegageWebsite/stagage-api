import factory
import random
from faker import Faker
from users.test.factories import UserFactory

fake = Faker()


class ArtistFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'stagegage.Artist'
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'test_artist_{}'.format(n))


class FestivalFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'stagegage.Festival'
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'test_festival_{}'.format(n))
    start_date = fake.date()

    @factory.post_generation
    def artists(self, create, extraced, **kwargs):
        if not create:
            return
        if extraced:
            for artist in extraced:
                self.artists.add(artist)

class RankingFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'stagegage.Ranking'

    score = random.uniform(0,10)
    festival = factory.SubFactory(FestivalFactory)
    artist = factory.SubFactory(ArtistFactory)
    user = factory.SubFactory(UserFactory)

