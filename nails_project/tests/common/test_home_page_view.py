from nails_project.sonq_nails.models import Nails
from tests.base.mixins import UserTestUtils, NailsTestUtils
from tests.base.tests import NailsProjectTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class HomePageTests(NailsProjectTestCase, UserTestUtils, NailsTestUtils):

    def test_homePageVieName_and_templateName(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='nails/index.html')

    def test_homePageView_withNoFeedback(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(0, len(list(response.context['nails'])))

    def test_homePageView_withFeedback(self):
        self.client.force_login(self.user)
        nails_user = self.create_user(email='nails@user.com', password='12345qwe', is_active=True)
        nails = self.create_nails(
            type=Nails.MANICURE,
            feedback='Test',
            description='TEst nails description',
            image='path/to/image.png',
            user=nails_user,
        )
        response = self.client.get(reverse('home'))
        self.assertEqual(1, len(list(response.context['nails'])))
