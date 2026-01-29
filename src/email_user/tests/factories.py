import factory
from factory.declarations import LazyAttribute
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

    @factory.post_generation  # type: ignore[attr-defined,untyped-decorator]
    def password(self: models.EmailUser, create, extracted, **kwargs):
        pw = extracted or EmailUserFactory.PASSWORD
        self.set_password(pw)
        if create:
            self.save(update_fields=["password"])
