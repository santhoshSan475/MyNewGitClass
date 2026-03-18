from django.db import models

# Create your models here.


class CricketPlayerTable(models.Model):
    playerName = models.CharField(max_length=150)
    JerseyNo = models.IntegerField()
    country = models.CharField(max_length=150)
    playerType = models.CharField(max_length=150)

    def __str__(self):
        return self.playerName


