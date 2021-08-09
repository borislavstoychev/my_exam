from nails_project.common.models import Comment
from nails_project.sonq_nails.models import Nails, Like
from tests.base.mixins import UserTestUtils, NailsTestUtils
from tests.base.tests import NailsProjectTestCase
from django.core.exceptions import ValidationError


class CommentModelTests(NailsTestUtils, UserTestUtils, NailsProjectTestCase):

    def test_saveModel_whenValid_shouldBeValid(self):
        nails_user = self.create_user(email='nails@user.com', password='12345qwe', is_active=True)
        nails = self.create_nails(
            type=Nails.MANICURE,
            feedback='Test',
            description='Test nails description',
            image='path/to/image.png',
            user=nails_user,
        )
        data = {
            'nails': nails,
            'comment': 'beautiful',
            'user': self.user,
        }
        obj = Comment(**data)
        obj.full_clean()
        obj.save()
        self.assertEqual(nails, obj.nails)
        self.assertEqual(self.user, obj.user)
        self.assertTrue(Comment.objects.filter(nails_id=nails.id).exists())

    def test_saveModel_whenInvalid_shouldBeInvalid_nailsError(self):

        data = {
            'nails': None,
            'comment': 'beautiful',
            'user': self.user,
        }
        with self.assertRaises(ValidationError) as error:
            obj = Comment(**data)
            obj.full_clean()
            obj.save()
        self.assertIsNotNone(error)
        # self.assertNotEqual(nails.like_set, 0)
        self.assertFalse(Comment.objects.filter(pk=self.user.id).exists())

    def test_saveModel_whenInvalid_shouldBeInvalid_commentError(self):
        nails_user = self.create_user(email='nails@user.com', password='12345qwe', is_active=True)
        nails = self.create_nails(
            type=Nails.MANICURE,
            feedback='Test',
            description='Test nails description',
            image='path/to/image.png',
            user=nails_user,
        )
        data = {
            'nails': nails,
            'comment': None,
            'user': self.user,
        }
        with self.assertRaises(ValidationError) as error:
            obj = Comment(**data)
            obj.full_clean()
            obj.save()
        self.assertIsNotNone(error)
        self.assertNotEqual(0, nails.comment_set)
        self.assertFalse(Comment.objects.filter(pk=nails.id).exists())

    def test_saveModel_whenInvalid_shouldBeInvalid_userError(self):
        nails_user = self.create_user(email='nails@user.com', password='12345qwe', is_active=True)
        nails = self.create_nails(
            type=Nails.MANICURE,
            feedback='Test',
            description='Test nails description',
            image='path/to/image.png',
            user=nails_user,
        )
        data = {
            'nails': nails,
            'comment': "None",
            'user': None,
        }
        with self.assertRaises(ValidationError) as error:
            obj = Comment(**data)
            obj.full_clean()
            obj.save()
        self.assertIsNotNone(error)
        self.assertNotEqual(0, nails.comment_set)
        self.assertFalse(Comment.objects.filter(pk=nails.id).exists())