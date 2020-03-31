from django.db import models


# Create your models here.

class Destination(models.Model):
    id: int
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)