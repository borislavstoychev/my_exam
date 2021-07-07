from django.db import models


# Create your models here.

class Nail(models.Model):
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


class Like(models.Model):
    pet = models.ForeignKey(Nail, on_delete=models.CASCADE)
