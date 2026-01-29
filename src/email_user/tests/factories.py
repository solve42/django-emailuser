from factory.declarations import LazyAttribute, PostGenerationMethodCall
from factory.django import DjangoModelFactory
from factory.faker import Faker

from email_user import models


class EmailUserFactory(DjangoModelFactory):
    PASSWORD = "pw"

    class Meta(object):
        model = models.EmailUser
        exclude = ("PASSWORD",)
        django_get_or_create = ("email",)

    last_name = Faker("last_name")
    first_name = Faker("first_name")
    email = LazyAttribute(lambda self: "{0}@example.com".format(self.last_name))
    is_staff = False
    is_active = True
    password = PostGenerationMethodCall("set_password", PASSWORD)
