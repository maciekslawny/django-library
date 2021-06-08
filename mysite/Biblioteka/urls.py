from django.urls import path
from . import views

urlpatterns = [
    path('ksiazki/', views.ksiazki, name='ksiazki'),
    path('filmy/', views.filmy, name='filmy'),
    path('plyty/', views.plyty, name='plyty'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('wypozyczenia/', views.wypozyczenia, name='wypozyczenia'),
    path('wypozycz/<str:rodzaj>/<int:item_id>', views.wypozycz, name='wypozycz'),
    path('zwroc/<str:rodzaj>/<int:item_id>', views.zwroc, name='zwroc'),
    path('strona-edycja/', views.strona_edycja, name='strona-edycja'),
    path('<str:zadanie>/<str:rodzaj>/<int:item_id>', views.edycja, name='edycja'),
    path('statystyki/<str:date_from>/<str:date_to>', views.statystyki, name='statystyki'),
        
]