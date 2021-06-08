from django.contrib import admin
from .models import Ksiazka, Film, Plyta, Wypozyczenie
# Register your models here.

admin.site.register(Ksiazka)
admin.site.register(Film)
admin.site.register(Plyta)
admin.site.register(Wypozyczenie)