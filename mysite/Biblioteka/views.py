from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from .models import Ksiazka, Film, Plyta, Wypozyczenie
from django.contrib.auth import authenticate, login, logout
import datetime
from django.views.generic.detail import DetailView
# Create your views here.

class Ksiazki(View):
    def get(self, request):
        try:
            ksiazki = get_list_or_404(Ksiazka, wypozyczajacy=None)
        except:
            ksiazki = None
        return render(request, 'biblioteka/ksiazki.html', {'ksiazki': ksiazki})

class Filmy(View):
    def get(self, request):
        try:
            filmy = get_list_or_404(Film, wypozyczajacy=None)
        except:
            filmy = None
        return render(request, 'biblioteka/filmy.html', {'filmy': filmy})
        


class Plyty(View):
    def get(self, request):
        try:
            plyty = get_list_or_404(Plyta, wypozyczajacy=None)
        except:
            plyty = None
        return render(request, 'biblioteka/muzyka.html', {'plyty': plyty})


class Edycja(View):

    def dispatch(self, request, zadanie, rodzaj, item_id):
        if rodzaj == 'ksiazki':
            autor = request.POST.get('autor')
            tytul = request.POST.get('tytul')
            gatunek = request.POST.get('gatunek')
            isbn = request.POST.get('isbn')
            wypozyczajacy = request.POST.get('wypozyczajacy')
            if zadanie == 'dodaj':
                try:
                    ksiazka = Ksiazka.objects.create(autor=autor, tytul=tytul, gatunek=gatunek, ISBN=isbn,)
                    ksiazka.save()
                except:
                    return redirect('strona-edycja')
            elif zadanie == 'edycja':
                ksiazka = Ksiazka.objects.get(id = item_id)
                
                ksiazka.autor = autor
                ksiazka.tytul = tytul
                ksiazka.gatunek = gatunek
                ksiazka.ISBN = isbn
                try:
                    ksiazka.save()
                except:
                    return redirect('strona-edycja')
            elif zadanie == 'usun':
                ksiazka = Ksiazka.objects.get(id = item_id)
                ksiazka.delete()

        elif rodzaj == 'filmy':
            rezyser = request.POST.get('rezyser')
            tytul = request.POST.get('tytul')
            gatunek = request.POST.get('gatunek')
            czas_trwania = request.POST.get('czas_trwania')
            wypozyczajacy = request.POST.get('wypozyczajacy')

            #Sprawdzenie czy wybrany gatunek jest większy o 3 od najmniejszego
            filmy = get_list_or_404(Film)
            lista_gatunkow = {}
            najmniejszy = {'nazwa': 'brak',
                        'liczba': 9999}
            for film in filmy:
                if film.gatunek in lista_gatunkow:
                    lista_gatunkow[f'{film.gatunek}'] += 1
                else:
                    lista_gatunkow[f'{film.gatunek}'] = 1     
            for item in lista_gatunkow:
                if lista_gatunkow[f'{item}'] < najmniejszy['liczba']:
                    najmniejszy['liczba'] = lista_gatunkow[f'{item}']
                    najmniejszy['nazwa'] = item
            if gatunek in lista_gatunkow and (lista_gatunkow[f'{gatunek}'] - najmniejszy['liczba'])>=3:
                print('ROZNICA = ', (lista_gatunkow[f'{gatunek}'] - najmniejszy['liczba']))
                return redirect('strona-edycja')
            print(lista_gatunkow, najmniejszy)


            if zadanie == 'dodaj':
                try:
                    film = Film.objects.create(rezyser=rezyser, tytul=tytul, gatunek=gatunek, czas_trwania=czas_trwania,)
                    film.save()
                except:
                    return redirect('strona-edycja')
            elif zadanie == 'edycja':
                film = Film.objects.get(id = item_id)
                film.rezyser = rezyser
                film.tytul = tytul
                film.gatunek = gatunek
                film.czas_trwania = czas_trwania
                try:
                    film.save()
                except:
                    return redirect('strona-edycja')
            elif zadanie == 'usun':
                film = Film.objects.get(id = item_id)
                film.delete()

        elif rodzaj == 'plyty':
            zespol = request.POST.get('zespol')
            tytul = request.POST.get('tytul')
            gatunek = request.POST.get('gatunek')
            lista_utworow = request.POST.get('lista_utworow')
            czas_trwania = request.POST.get('czas_trwania')
            wypozyczajacy = request.POST.get('wypozyczajacy')

            # sprawdza czy w ramach jednego gatunku nie ma tej samej listy utworów
            try:
                plyty = get_list_or_404(Plyta)
            except:
                plyty = []
            for plyta in plyty:
                if plyta.gatunek == gatunek and plyta.lista_utworow == lista_utworow and item_id != plyta.id:
                    print('Lista utworow już jest w tym gatunku')
                    return redirect('strona-edycja')
            
            lista_gatunkow = []
            for plyta in plyty:
                if plyta.zespol == zespol:
                    if plyta.gatunek not in lista_gatunkow:
                        lista_gatunkow.append(plyta.gatunek)
            if len(lista_gatunkow)>=2 and gatunek not in lista_gatunkow:
                print('zespół ma już 2 płyty w innych gatunki')
                return redirect('strona-edycja')


            if zadanie == 'dodaj':
                try:
                    plyta = Plyta.objects.create(zespol=zespol, tytul=tytul, gatunek=gatunek, lista_utworow=lista_utworow, czas_trwania=czas_trwania)
                    plyta.save()
                except:
                    return redirect('strona-edycja')
            elif zadanie == 'edycja':
                plyta = Plyta.objects.get(id = item_id)
                
                plyta.zespol = zespol
                plyta.tytul = tytul
                plyta.gatunek = gatunek
                plyta.lista_utworow = lista_utworow
                plyta.czas_trwania = czas_trwania
                try:
                    plyta.save()
                except:
                    return redirect('strona-edycja')
            elif zadanie == 'usun':
                plyta = Plyta.objects.get(id = item_id)
                plyta.delete()

        return redirect('strona-edycja')

class Wypozycz(DetailView):

    def get(self, request, rodzaj, item_id):
        username = request.user 
        wypozyczenie = Wypozyczenie.objects.create(rzecz=rodzaj, item_id=item_id, data_wypozyczenia=datetime.datetime.now(), wypozyczajacy=username,)

        if rodzaj == 'ksiazki':
            print(rodzaj, item_id)
            item = Ksiazka.objects.get(id = item_id)
            item.wypozyczajacy = username
            item.save()
        elif rodzaj == 'filmy':
            item = Film.objects.get(id = item_id)
            item.wypozyczajacy = username
            item.save()
        elif rodzaj == 'plyty':
            item = Plyta.objects.get(id = item_id)
            item.wypozyczajacy = username
            item.save()

        wypozyczenie.gatunek = item.gatunek  
        wypozyczenie.tytul = item.tytul
        wypozyczenie.save()
        return redirect(f'{rodzaj}')



class Zwroc(View):
    def get(self, request, rodzaj, item_id):
        try:
            wypozyczenie = Wypozyczenie.objects.get(item_id = item_id, data_zwrotu = None)  
            wypozyczenie.data_zwrotu = datetime.datetime.now()
            wypozyczenie.save()
        except:
            pass
        if rodzaj == 'ksiazki':
            print(rodzaj, item_id)
            item = Ksiazka.objects.get(id = item_id)
            item.wypozyczajacy = None
            item.save()
        elif rodzaj == 'filmy':
            item = Film.objects.get(id = item_id)
            item.wypozyczajacy = None
            item.save()
        elif rodzaj == 'plyty':
            item = Plyta.objects.get(id = item_id)
            item.wypozyczajacy = None
            item.save()
        return redirect('wypozyczenia')

class StronaEdycja(View):
    
    def get(self, request):
        if request.user.is_superuser:
            try:
                ksiazki = get_list_or_404(Ksiazka)
            except:
                ksiazki = None
            try:
                filmy = get_list_or_404(Film)
            except:
                filmy = None
            try:
                plyty = get_list_or_404(Plyta)
            except:
                plyty = None
            return render(request, 'biblioteka/edycja_admin.html', {'ksiazki': ksiazki, 'filmy': filmy, 'plyty': plyty})
        else:
            return redirect('wypozyczenia')

class Wypozyczenia(View):
    def get(self, request):
            username = request.user
            try:
                ksiazki = get_list_or_404(Ksiazka, wypozyczajacy=username)       
            except:
                ksiazki = None     
            try:
                filmy = get_list_or_404(Film, wypozyczajacy=username)
            except:
                filmy = None
            try:
                plyty = get_list_or_404(Plyta, wypozyczajacy=username)
            except:
                plyty = None
            return render(request, 'biblioteka/wypozyczenia.html', {'ksiazki': ksiazki,'filmy':filmy, 'plyty':plyty})



class Statystyki(View):
    def dispatch(self, request, date_from, date_to):
        if request.method == 'POST':
            date_from = request.POST.get('date_from')
            date_to = request.POST.get('date_to')
           
        wypozyczenia = get_list_or_404(Wypozyczenie)
        date_from = datetime.datetime.strptime(date_from, "%Y-%m-%d")
        date_to = datetime.datetime.strptime(date_to, "%Y-%m-%d")
        wypozyczenia_ksiazki = []
        gatunek_ksiazki = {}
        wypozyczenia_filmy = []
        gatunek_filmy = {}
        wypozyczenia_muzyka = []
        gatunek_muzyka = {}
        for item in wypozyczenia:
            item_date = datetime.datetime.strptime(str(item.data_wypozyczenia)[0:10], "%Y-%m-%d") 
            if (item_date > date_from and item_date < date_to):
                if item.rzecz == 'ksiazki':
                    item = {'id': item.id, 'gatunek': item.gatunek, 'wypozajacy': item.wypozyczajacy}
                    wypozyczenia_ksiazki.append(item)
                elif item.rzecz == 'filmy':
                    item = {'id': item.id, 'gatunek': item.gatunek, 'wypozajacy': item.wypozyczajacy}
                    wypozyczenia_filmy.append(item)
                elif item.rzecz == 'plyty':
                    item = {'id': item.id, 'gatunek': item.gatunek, 'wypozajacy': item.wypozyczajacy}
                    wypozyczenia_muzyka.append(item)

        for item in wypozyczenia_ksiazki:
            if item['gatunek'] in gatunek_ksiazki:
                gatunek_ksiazki[f"{item['gatunek']}"] += 1
            else:
                gatunek_ksiazki[f"{item['gatunek']}"] = 1
        for item in wypozyczenia_filmy:
            if item['gatunek'] in gatunek_filmy:
                gatunek_filmy[f"{item['gatunek']}"] += 1
            else:
                gatunek_filmy[f"{item['gatunek']}"] = 1
        for item in wypozyczenia_muzyka:
            if item['gatunek'] in gatunek_muzyka:
                gatunek_muzyka[f"{item['gatunek']}"] += 1
            else:
                gatunek_muzyka[f"{item['gatunek']}"] = 1

        gatunek_ksiazki = sorted(gatunek_ksiazki.items(), key=lambda x: x[1], reverse=True)
        gatunek_filmy = sorted(gatunek_filmy.items(), key=lambda x: x[1], reverse=True)  
        gatunek_muzyka = sorted(gatunek_muzyka.items(), key=lambda x: x[1], reverse=True)

        return render(request, 'biblioteka/statystyki.html', {'gatunek_ksiazki': gatunek_ksiazki, 'gatunek_filmy': gatunek_filmy, 'gatunek_muzyka': gatunek_muzyka, 'date_from': str(date_from)[0:10], 'date_to': str(date_to)[0:10]})      

class LoginPage(View):
    def dispatch(self, request):
        if request.user.is_authenticated:
            return redirect('ksiazki')
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password = password)
                
                if user is not None:
                    login(request, user)
                    return redirect('ksiazki')
        return render(request, 'biblioteka/login.html')


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('loginPage')

