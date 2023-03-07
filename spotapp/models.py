from django.db import models
from django_resized import ResizedImageField
from taggit.managers import TaggableManager

from spotapp import constants

# Create your models here.


class Drink(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    ingredients = TaggableManager()
    drink_tag = models.CharField(
        max_length=50, choices=constants.DRINK_TYPES, null=True, blank=True)

    def __str__(self):
        return f"{self.name} | {self.drink_tag}"


class Review(models.Model):
    drink = models.ForeignKey(Drink, models.DO_NOTHING)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.drink)} | {self.rate}'
