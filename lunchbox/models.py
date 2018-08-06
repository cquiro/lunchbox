from .utils import ChoiceEnum
from django.conf import settings
from django.db import models


class Menu(models.Model):
    date = models.DateTimeField('menu date')

    def name(self):
        return 'Today\'s Menu (' + self.date.strftime('%A %d %B %Y') + ')'

    def __str__(self):
        return self.name()


class Option(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Sizes(ChoiceEnum):
    XL = 'Extra Large'
    NL = 'Normal'


class Choice(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    eater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    preferences = models.CharField(max_length=200)
    size = models.CharField(max_length=2, choices=Sizes.choices(), default=Sizes.NL)

