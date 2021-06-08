from django.db import models
from django.conf import settings
# Create your models here.





class Ksiazka(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=200)
    tytul = models.CharField(max_length=200)
    gatunek = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)
    wypozyczajacy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        unique_together = ('autor', 'tytul', 'gatunek',)

    def __str__(self):
        return self.tytul



class Film(models.Model):
    rezyser = models.CharField(max_length=200)
    tytul = models.CharField(max_length=200)
    gatunek = models.CharField(max_length=200) 
    czas_trwania = models.IntegerField()
    wypozyczajacy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        unique_together = ('rezyser', 'tytul', 'czas_trwania',)
    


    def __str__(self):
        return self.tytul

class Plyta(models.Model):
    zespol = models.CharField(max_length=200)
    tytul = models.CharField(max_length=200)
    gatunek = models.CharField(max_length=200)
    lista_utworow = models.CharField(max_length=200)
    czas_trwania = models.IntegerField()
    wypozyczajacy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.tytul


class Wypozyczenie(models.Model):
    tytul = models.CharField(max_length=200, blank=True, null=True)
    gatunek = models.CharField(max_length=200, blank=True, null=True)
    rzecz = models.CharField(max_length=200)
    item_id = models.IntegerField()
    data_wypozyczenia = models.DateTimeField()
    data_zwrotu = models.DateTimeField(blank=True, null=True)
    wypozyczajacy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.tytul