from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

UserModel = get_user_model()


class Nails(models.Model):
    PEDICURE = 'pedicure'
    MANICURE = 'manicure'
    ELSE = 'else'
    NAILS_TYPE = (
        (PEDICURE, "Pedicure"),
        (MANICURE, 'Manicure'),
        (ELSE, 'Else'),
    )
    type = models.CharField(max_length=10, choices=NAILS_TYPE, default=ELSE)
    title = models.CharField(max_length=7)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images/nails')
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    pet = models.ForeignKey(Nails, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

