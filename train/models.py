from django.db import models

# Create your models here.
class Poses(models.Model):
    name = models.CharField(max_length=20)
    

class Move(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    poses = models.ManyToManyField("train.Poses")
