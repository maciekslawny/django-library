from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from .models import Ksiazka
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return HttpResponse("Witaj na stronie biblioteki.")

@login_required(login_url='loginPage')
def ksiazki(request):
    try:
        ksiazki = get_list_or_404(Ksiazka, wypozyczajacy=None)
    except:
        ksiazki = None
    return render(request, 'biblioteka/ksiazki.html', {'ksiazki': ksiazki})

def wypozycz(request, rodzaj, item_id):
    username = request.user
    if rodzaj == 'ksiazki':
        print(rodzaj, item_id)
        item = Ksiazka.objects.get(id = item_id)
        item.wypozyczajacy = username
        item.save()
    return redirect('ksiazki')


def zwroc(request, rodzaj, item_id):
    if rodzaj == 'ksiazki':
        print(rodzaj, item_id)
        item = Ksiazka.objects.get(id = item_id)
        item.wypozyczajacy = None
        item.save()
    return redirect('wypozyczenia')



@login_required(login_url='loginPage')
def wypozyczenia(request):
    username = request.user
    try:
        ksiazki = get_list_or_404(Ksiazka, wypozyczajacy=username)
    except:
        ksiazki = None
    return render(request, 'biblioteka/wypozyczenia.html', {'ksiazki': ksiazki})



def loginPage(request):
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

def logoutUser(request):
    logout(request)
    return redirect('loginPage')
