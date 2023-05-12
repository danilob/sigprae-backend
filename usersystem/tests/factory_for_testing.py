from datetime import datetime
from datetime import timedelta
import random

#https://factoryboy.readthedocs.io/en/stable/index.html
import factory
from faker import Faker
from usersystem.models import User

#https://pypi.org/project/validate-docbr/
from validate_docbr import CPF

def unique_first_name():
    """Localized pt_BR first_name with unique values"""
    faker = Faker('pt_BR')
    return faker.unique.first_name()

class _UserFactoryBoy(factory.django.DjangoModelFactory):
    """Using factoryboy and faker to create test factory"""
    class Meta:
        model = 'usersystem.User'
    
    username = factory.LazyFunction(unique_first_name)
    password = factory.Faker('password')
    full_name = factory.Faker('name')
    #gender = M | F | O
    genre = factory.LazyFunction(lambda: random.choice(User.USER_GENRE)[0])
    birth_date = factory.Faker('date_between',
                               start_date='-20y',
                               end_date=datetime(year=2004, month=1, day=1))
    #cpf = factory.Faker('cpf')
    phone_number = "DD111111111"
    email = factory.Faker('email')
    profile = factory.LazyFunction(lambda: random.choice(User.USER_PROFILE)[0])
    cpf = "11111111111"


class UserFactory:
    """Object to create User for testing purposes"""

    @classmethod
    def create_valid_instance(cls, **kwargs):
        return _UserFactoryBoy.create(**kwargs)

