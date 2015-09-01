import factory
from faker import Faker
from users.test.factories import UserFactory

fake = Faker()


class ArtistFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'stagegage.Artist'
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'test_artist_{}'.format(n))

    @factory.post_generation
    def festivals(self, create, extraced, **kwargs):
        if not create:
            return
        if extraced:
            for festival in extraced:
                self.festivals.add(festival)

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