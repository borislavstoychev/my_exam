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


class Schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"On Date:{self.date.strftime('%m/%d/%Y')} Available hour:{self.time.strftime('%H:%M')}"
