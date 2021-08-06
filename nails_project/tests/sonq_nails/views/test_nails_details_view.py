from django.urls import reverse

from nails_project.common.models import Comment
from nails_project.sonq_nails.models import Nails, Like
from tests.base.mixins import NailsTestUtils, UserTestUtils
from tests.base.tests import NailsProjectTestCase


class NailsDetailsTest(NailsTestUtils, UserTestUtils, NailsProjectTestCase):
    def test_getNailsDetails_whenNailsDoesNotExists(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('nails details', kwargs={
            'pk': 1,
        }))

        self.assertEqual(404, response.status_code)

    def test_getNailsDetails_whenNailsExistsAndIsOwner_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        nails = self.create_nails(
            type=Nails.MANICURE,
            feedback='Test',
            description='TEst nails description',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.get(reverse('nails details', kwargs={
            'pk': nails.id,
        }))

        self.assertTrue(response.context['is_owner'])
        self.assertFalse(response.context['comments'])
        self.assertTrue(response.context['comment_form'])
        self.assertFalse(response.context['is_liked_by_user'])

    def test_getNailsDetails_whenNailsExistsAndIsNotOwnerAndNotLiked_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        nails_user = self.create_user(email='nails@user.com', password='12345qwe', is_active=True)
        nails = self.create_nails(
            type=Nails.MANICURE,
            feedback='Test',
            description='TEst nails description',
            image='path/to/image.png',
            user=nails_user,
        )

        response = self.client.get(reverse('nails details', kwargs={
            'pk': nails.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked_by_user'])
        self.assertFalse(response.context['comments'])
        self.assertTrue(response.context['comment_form'])

    def test_getNailsDetails_whenNailsExistsAndIsNotOwnerAndLiked_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        nails_user = self.create_user(email='nails@user.com', password='12345qwe', is_active=True)
        nails = self.create_nails_with_like(
            like_user=self.user,
            type=Nails.MANICURE,
            feedback='Test',
            description='TEst nails description',
            image='path/to/image.png',
            user=nails_user,
        )

        response = self.client.get(reverse('nails details', kwargs={
            'pk': nails.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertTrue(response.context['is_liked_by_user'])
        self.assertFalse(response.context['comments'])
        self.assertTrue(response.context['comment_form'])

    def test_commentNails_whenNailsHasOwner_shouldReturnComment(self):
        self.client.force_login(self.user)
        nails_user = self.create_user(email='nails@user.com', password='12345qwe', is_active=True)
        nails = self.create_nails_with_comment(
            comment_user=self.user,
            type=Nails.MANICURE,
            feedback='Test',
            description='Test nails description',
            image='path/to/image.png',
            user=nails_user,
        )

        response = self.client.get(reverse('nails details', kwargs={
            'pk': nails.id,
        }))

        self.assertEqual(200, response.status_code)

        comment_exists = Comment.objects.filter(
            comment='bravo!',
            user_id=self.user.id,
            nails_id=nails.id,
        ) \
            .exists()

        self.assertTrue(comment_exists)

