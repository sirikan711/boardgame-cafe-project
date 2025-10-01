# boardgames/models.py
from django.db import models

class BoardGame(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    )
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    players_min = models.IntegerField()
    players_max = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.name