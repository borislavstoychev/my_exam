from django.db import models
from django.contrib.auth import get_user_model
from nails_project.sonq_nails.models import Nails


# Create your models here.

UserModel = get_user_model()


class Comment(models.Model):
    nails = models.ForeignKey(Nails, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
