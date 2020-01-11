from django.db import models

# Create your models here.

class Riddle(models.Model):
    lead = models.CharField(max_length=100)
    num = models.IntegerField()
    img = models.CharField(max_length=100)
    team = models.CharField(max_length=20)
    isOpen = models.BooleanField(default=False)
    numAttemp = models.IntegerField(default=0)
    isSolved = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    sub = models.IntegerField(default=0)
    mag_c = models.IntegerField(default=3)


class Submit(models.Model):
    u_show = models.CharField(max_length=20)
    r_num = models.IntegerField()
    r_team = models.CharField(max_length=20)

class serial(models.Model):
    serial = models.IntegerField(default=1)
