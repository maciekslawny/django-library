from django.urls import path

from .views import Ksiazki, Filmy, Plyty, Wypozyczenia, LogoutUser, Wypozycz, Zwroc, StronaEdycja, Statystyki, Edycja, LoginPage
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('ksiazki/', login_required(login_url='loginPage')(Ksiazki.as_view()), name='ksiazki'),
    path('filmy/', login_required(login_url='loginPage')(Filmy.as_view()), name='filmy'),   
    path('plyty/', login_required(login_url='loginPage')(Plyty.as_view()), name='plyty'),
    path('login/', LoginPage.as_view(), name='loginPage'),    
    path('logout/', LogoutUser.as_view(), name='logoutUser'),
    path('wypozyczenia/', login_required(login_url='loginPage')(Wypozyczenia.as_view()), name='wypozyczenia'),
    path('wypozycz/<str:rodzaj>/<int:item_id>', Wypozycz.as_view(), name='wypozycz'),
    path('zwroc/<str:rodzaj>/<int:item_id>', Zwroc.as_view(), name='zwroc'),
    path('strona-edycja/', login_required(login_url='loginPage')(StronaEdycja.as_view()), name='strona-edycja'),
    path('<str:zadanie>/<str:rodzaj>/<int:item_id>', Edycja.as_view(), name='edycja'),
    path('statystyki/<str:date_from>/<str:date_to>', login_required(login_url='loginPage')(Statystyki.as_view()), name='statystyki'),

        
]