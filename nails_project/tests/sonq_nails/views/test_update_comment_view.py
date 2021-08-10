from django.urls import reverse

from nails_project.common.models import Comment
from nails_project.sonq_nails.models import Nails, Like
from tests.base.mixins import UserTestUtils, NailsTestUtils
from tests.base.tests import NailsProjectTestCase


class CommentUpdateViewTests(NailsTestUtils, UserTestUtils, NailsProjectTestCase):
    def test_updateCommentNails_whenNailsOwner_shouldUpdateComment(self):
        self.client.force_login(self.user)
        nails_user = self.create_user(email='nails@user.com', password='12345qwe', is_active=True)
        nails = self.create_nails_with_comment(
            type=Nails.MANICURE,
            feedback='Test',
            description='Test nails description',
            image='path/to/image.png',
            user=nails_user,
            comment_user=self.user
        )
        comment_id = Comment.objects.get(user_id=self.user.id).id
        response = self.client.post(reverse('update comment', kwargs={
            'pk': comment_id,
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

    def test_updateCommentNails_whenNotNailsOwner_shouldBeForbidden(self):
        nails_user = self.create_user(email='nails@user.com', password='12345qwe', is_active=True)
        nails = self.create_nails_with_comment(
            type=Nails.MANICURE,
            feedback='Test',
            description='Test nails description',
            image='path/to/image.png',
            user=nails_user,
            comment_user=self.user
        )
        comment_id = Comment.objects.get(user_id=self.user.id).id
        self.client.force_login(nails_user)
        response = self.client.post(reverse('update comment', kwargs={
            'pk': comment_id,
        }),  data={
            'comment': 'test'
        })

        self.assertEqual(403, response.status_code)

        comment_exists = Comment.objects.filter(
            comment='test',
            user_id=self.user.id,
            nails_id=nails.id,
        ) \
            .exists()

        self.assertFalse(comment_exists)