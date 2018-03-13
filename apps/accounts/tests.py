# Native Python Modules.

# External Modules.

# Django Modules.

# Project Modules.
from core import base_tests
from apps.accounts import models, serializers


class AccountTestCase(base_tests.ModelsBaseTestCase):

    model = models.Account
    models.Account._meta
    serializer = serializers.AccountSerializer
    url = "/accounts"
    get_dict = {
        "gender": int,
        "firstname": str,
        "lastname": str,
        "email": str,
        "birthdate": str,
    }

    @property
    def post_data(self):
        return {
            "gender": 0,
            "firstname": "Hovhannes",
            "lastname": "Dabaghyan",
            "email": "hovhannes.dabaghyan@gmail.com",
            "birthdate": "1992-02-29",
        }

    def setUp(self):
        obj = models.Account(gender=1,
                             firstname="John",
                             lastname="Doe",
                             email="example@example.com",
                             birthdate="1990-01-12")
        obj.save()
        self.to_update_id = obj.id
        self.deletable_id = obj.id
        self.patch_data = self.duplicated_data = self.generate_duplication_data(obj)
