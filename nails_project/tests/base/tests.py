from django.contrib.auth import get_user_model
from django.test import TestCase, Client

UserModel = get_user_model()


class NailsProjectTestCase(TestCase):
    logged_in_user_email = 'testuser'
    logged_in_user_password = '12345'

    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )
        self.user.is_active = True
        self.user.save()