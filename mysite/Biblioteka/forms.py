from django import forms

class DodajKsiazke(forms.Form):
    autor = forms.CharField(label='Your name', max_length=100)
    tytul = forms.CharField(label='Your name', max_length=100)
    gatunek = forms.CharField(label='Your name', max_length=100)
    ISBN = forms.CharField(label='Your name', max_length=100)