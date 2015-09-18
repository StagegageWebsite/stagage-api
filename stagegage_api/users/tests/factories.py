import factory
from faker import Faker

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: 'testuser{}'.format(n))
    password = factory.PostGenerationMethodCall('set_password', fake.password())
    email = factory.lazy_attribute(lambda s: fake.email())
    first_name = factory.lazy_attribute(lambda s: fake.first_name())
    last_name = factory.lazy_attribute(lambda s: fake.last_name())
    is_active = True
    is_staff = False


class AdminFactory(UserFactory):
    #TODO: admin factory
    pass


