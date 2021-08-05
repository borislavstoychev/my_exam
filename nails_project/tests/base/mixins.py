from django.contrib.auth import get_user_model

from nails_project.sonq_nails.models import Nails, Like

UserModel = get_user_model()


class NailsTestUtils:

    def create_nails(self, **kwargs):
        return Nails.objects.create(**kwargs)

    def create_nails_with_like(self, like_user, **kwargs):
        nails = self.create_nails(**kwargs)
        Like.objects.create(
            nails=nails,
            user=like_user,
        )
        return nails


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)