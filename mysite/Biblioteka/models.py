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
    
    # ale ja w 1 zrobiłem tak że biorę gatunek filmu który chce teraz zapisać, biere też gatunek który ma najmniej filmów, odejmuję liczbę filmów w jednym gatunku od liczby w drugim i jak różnica == 3 to już jest za duża różnica i nie zapisuje filmu

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

    #W drugim można po chamsku zrobić pętle w pętli, w pierwszej iter. po gatunkach, w drugiej iter. po zespołach i sprawdzać czy zespół był już w 2 gatunkach, jak po zapisie będzie w 3 to RIP. Za to już mi obciął punkty, bo pętla w pętli to cringe