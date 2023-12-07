from django.db import models

class Car(models.Model):
    marque = models.CharField(max_length=45)
    modele = models.CharField(max_length=45, verbose_name="Modèle")
    annee = models.IntegerField(verbose_name="Année")
    cylindree = models.IntegerField(verbose_name="Cylindrée en cm3")
    version = models.CharField(max_length=45)
