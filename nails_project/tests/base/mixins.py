from django.contrib.auth import get_user_model

from nails_project.common.models import Comment, Schedule
from nails_project.sonq_nails.models import Nails, Like

UserModel = get_user_model()


class NailsTestUtils:

    def create_nails(self, **kwargs):
        return Nails.objects.create(**kwargs)

    def create_nails_with_comment(self, comment_user, **kwargs):
        nails = self.create_nails(**kwargs)
        Comment.objects.create(
            comment='bravo!',
            nails=nails,
            user=comment_user
        )
        return nails

    def create_nails_with_like(self, like_user, **kwargs):
        nails = self.create_nails(**kwargs)
        Like.objects.create(
            nails=nails,
            user=like_user,
        )
        return nails


class ScheduleTestUtils:

    def create_schedule(self, **kwargs):
        return Schedule.objects.create(**kwargs)


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)

    def create_superuser(self, **kwargs):
        return UserModel.objects.create_superuser