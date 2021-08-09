from django.dispatch import receiver
from django.db.models.signals import pre_save
from cloudinary import uploader
from nails_project.sonq_nails.models import Nails


@receiver(pre_save, sender=Nails)
def remove_old_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_image = Nails.objects.get(pk=instance.pk).image
        except Nails.DoesNotExist:
            return
        else:
            try:
                new_image = instance.image.url
            except AttributeError:
                uploader.destroy(old_image.public_id)

