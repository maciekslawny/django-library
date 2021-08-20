from typing import Sized
from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
import datetime
# Create your models here.

def current_year():
    return datetime.date.today().year


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notifications = models.BooleanField(blank=True, default=False)
    email = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'Profil użythownika {self.user.username}'

class Teczka(models.Model):
    CONTAINERS_TYPE = (
        ('40dv', '40 standard'),
        ('40hc', '40 high cube'),
        ('40rf', '40 reefer'),
        ('20dv', '20 standard'),
        ('20rf', '20 reefer'),
    )
    STATUS = (
        (None, 'Brak'),
        ('waiting', 'Do wprow.'),        
        ('submited', 'Wprowadzone'),
        ('checking', 'Wysł. do spr.'),
        ('amended', 'Popr. wprow.'),
        ('accepted', 'Zaakc.'),
        ('sent', 'Oryg. wysł.'),
    )
    SHIPOWNERS = (
        ('maersk', 'Maersk Line'),
        ('cma', 'CMA'),
        ('msc', 'MSC'),
        ('hapag', 'Hapag Lloyd'),
    )
    CASE_STATUS = (
        ('active', 'Aktywna'),
        ('ended', 'Zakończona'),
    )
    IMP_EXP = (
        ('imp', 'Import'),
        ('exp', 'Export'),
    )

    company = models.CharField(max_length=20, blank=True)
    shipowner = models.CharField(max_length=6, choices=SHIPOWNERS, blank=True)
    booking = models.CharField(max_length=20, blank=True)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    case_number = models.CharField(max_length=20, blank=True)
    offer_number = models.CharField(max_length=20, blank=True)
    year = models.IntegerField(default=1999, blank=True)
    cut_off = models.DateTimeField(null=True, blank=True)    
    etd = models.DateTimeField(null=True, blank=True)
    eta = models.DateTimeField(null=True, blank=True)
    loading_data = models.DateTimeField(null=True, blank=True)
    amount = models.IntegerField(default=0, blank=True)
    container_type = models.CharField(max_length=4, choices=CONTAINERS_TYPE, blank=True)
    loading_port = models.CharField(max_length=30, blank=True)
    load_place = models.CharField(max_length=20, blank=True)
    destination = models.CharField(max_length=20, blank=True)
    insurance = models.CharField(max_length=30, choices=STATUS, blank=True)
    si = models.CharField(max_length=30, choices=STATUS, blank=True)
    coo = models.CharField(max_length=30, choices=STATUS, blank=True)
    description = models.CharField(max_length=500, blank=True)
    customs = models.NullBooleanField(blank=True, default=False)
    vgm = models.BooleanField(blank=True, default=False)
    invoice = models.NullBooleanField(blank=True, default=False)
    case_status = models.CharField(max_length=10, choices=CASE_STATUS, blank=True, default='active')
    container_numbers = models.CharField(max_length=500, blank=True)
    import_export = models.CharField(max_length=3, choices=IMP_EXP, blank=True, default='exp')
    
    def __str__(self):
        return self.case_number

class Document(models.Model):
    case_number = models.ForeignKey(Teczka,
                            on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')
    file = models.FileField(upload_to='documents')
    name_file = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


