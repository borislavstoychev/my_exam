from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

from nails_project.accounts.models import Profile
from nails_project.sonq_nails.models import Nails

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = Profile(
            user=instance,
        )
        profile.save()


@receiver(pre_save, sender=Profile)
def check_is_complete(sender, instance, **kwargs):
    if instance.first_name and instance.last_name and instance.phone_number:
        instance.is_complete = True
    else:
        instance.is_complete = False

    if instance.pk:
        try:
            old_avatar = Profile.objects.get(pk=instance.pk).profile_image
        except Profile.DoesNotExist:
            return
        else:
            new_avatar = instance.profile_image
            if old_avatar and old_avatar.url != new_avatar.url:
                old_avatar.delete(save=False)


@receiver(pre_delete, sender=UserModel)
def delete_avatar_when_account_deleted(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_avatar = Profile.objects.get(pk=instance.pk).profile_image
            old_user_media = Nails.objects.filter(user_id=instance.pk)
        except Profile.DoesNotExist:
            return
        else:
            old_avatar.delete(save=False)
            for media in old_user_media:
                media.image.delete(save=False)
