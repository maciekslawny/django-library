from django.contrib import admin
from .models import Ksiazka, Film, CD
# Register your models here.

admin.site.register(Ksiazka)
admin.site.register(Film)
admin.site.register(CD)