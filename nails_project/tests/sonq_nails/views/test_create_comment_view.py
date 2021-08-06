from django.urls import reverse

from nails_project.common.models import Comment
from nails_project.sonq_nails.models import Nails, Like
from tests.base.mixins import UserTestUtils, NailsTestUtils
from tests.base.tests import NailsProjectTestCase


class CommentViewTests(NailsTestUtils, UserTestUtils, NailsProjectTestCase):
    def test_commentNails_whenNailsHasOwner_shouldCreateComment(self):
        self.client.force_login(self.user)
        nails_user = self.create_user(email='nails@user.com', password='12345qwe', is_active=True)
        nails = self.create_nails(
            type=Nails.MANICURE,
            feedback='Test',
            description='Test nails description',
            image='path/to/image.png',
            user=nails_user,
        )

        response = self.client.post(reverse('comment nails', kwargs={
            'pk': nails.id,
        }),  data={
            'comment': 'test'
        })

        self.assertEqual(302, response.status_code)

        comment_exists = Comment.objects.filter(
            comment='test',
            user_id=self.user.id,
            nails_id=nails.id,
        ) \
            .exists()

        self.assertTrue(comment_exists)

    def test_commentNails_whenCommentOwnerIsNone_shouldNotCreateComment(self):
        nails_user = self.create_user(email='nails@user.com', password='12345qwe', is_active=True)
        nails = self.create_nails(
            type=Nails.MANICURE,
            feedback='Test',
            description='Test nails description',
            image='path/to/image.png',
            user=nails_user,
        )

        response = self.client.post(reverse('comment nails', kwargs={
            'pk': nails.id,
        }),  data={
            'comment': 'test'
        })

        self.assertEqual(302, response.status_code)

        comment_exists = Comment.objects.filter(
            comment='test',
            user_id=self.user.id,
            nails_id=nails.id,
        ) \
            .exists()

        self.assertFalse(comment_exists)