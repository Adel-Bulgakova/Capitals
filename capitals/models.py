from django.db import models

class Capital(models.Model):
     question = models.CharField(max_length=200)
     answer = models.CharField(max_length=200)
     lat = models.FloatField(default=0)
     lng = models.FloatField(default=0)
     text = models.CharField(max_length=20000)
