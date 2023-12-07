from django.db import models

class Car(models.Model):
    marque = models.CharField(max_length=45)
    modele = models.CharField(max_length=45)
    annee = models.IntegerField()
    cylindree = models.IntegerField()
    version = models.CharField(max_length=45)
