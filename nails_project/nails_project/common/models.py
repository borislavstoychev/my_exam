from django.db import models

# Create your models here.
from nails_project.sonq_nails.models import Nail


class Comment(models.Model):
    nail = models.ForeignKey(Nail, on_delete=models.CASCADE)
    comment = models.TextField()
