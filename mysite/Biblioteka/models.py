from django.db import models
from django.conf import settings
# Create your models here.


class Ksiazka(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=200)
    tytul = models.CharField(max_length=200)
    gatunek = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13)
    #wypozyczajacy = models.CharField(max_length=13, blank=True, default='')
    wypozyczajacy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.tytul

class Film(models.Model):
    rezyser = models.CharField(max_length=200)
    tytul = models.CharField(max_length=200)
    gatunek = models.CharField(max_length=200)
    czas_trwania = models.IntegerField()
    def __str__(self):
        return self.tytul

class CD(models.Model):
    zespol = models.CharField(max_length=200)
    tytul = models.CharField(max_length=200)
    gatunek = models.CharField(max_length=200)
    lista_utworow = models.CharField(max_length=200)
    czas_trwania = models.IntegerField()
    def __str__(self):
        return self.tytul

