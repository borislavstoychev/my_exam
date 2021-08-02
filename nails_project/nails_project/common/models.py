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
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    available = models.BooleanField(default=False)

    def __str__(self):
        if self.start_time and self.end_time:
            return f"Date:{self.date.strftime('%d/%m')} {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"
        else:
            return f"Date:{self.date.strftime('%d/%m')} Not available!"

