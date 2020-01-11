from django.db import models

class record(models.Model):
    team = models.CharField(max_length=20)
    puzz = models.IntegerField()
    attemp = models.IntegerField()
    leader = models.CharField(max_length=100)


