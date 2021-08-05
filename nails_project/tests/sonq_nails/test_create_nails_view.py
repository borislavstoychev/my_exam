from django.urls import reverse

from nails_project.sonq_nails.models import Nails, Like
from tests.base.mixins import NailsTestUtils, UserTestUtils
from tests.base.tests import NailsProjectTestCase


class NailsCreateTest(NailsTestUtils, UserTestUtils, NailsProjectTestCase):

    def test_createNails_whenUserExist_shouldRedirectToNailsDetails(self):
        self.client.force_login(self.user)
        data ={
            "type": 'Manicure',
            'feedback': 'Test',
            'description': 'TEst nails description',
            'image': 'path/to/image.png',
            'use': self.user,
        }

        response_get = self.client.get(reverse('create nails'))
        self.assertEqual(200, response_get.status_code)
        response_post = self.client.post(reverse('create nails'), data=data)
        self.assertEqual(200, response_post.status_code)

    def test_creatNails_whenUserNotExist_shouldBeRedirectToSignIn(self):
        data = {
            "type": 'Manicure',
            'feedback': 'Test',
            'description': 'TEst nails description',
            'image': 'path/to/image.png',
            'use': self.user,
        }

        response_get = self.client.get(reverse('create nails'))
        self.assertEqual(302, response_get.status_code)
        self.assertEqual('/account/sign-in/?next=/nails/create/', response_get.url)