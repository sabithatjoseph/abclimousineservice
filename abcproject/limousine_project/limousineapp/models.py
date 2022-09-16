from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class findyourcar(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery')
    rateperhour = models.IntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.name



