from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('validacao/', views.validacao, name='validacao'),
    path('erro/', views.erro, name='erro'),
    path('inicio/', views.index, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('apagar/', views.apagar, name='apagar'),
    path('animais/', views.animais, name='animais'),
    path('animais/carregar/', views.carregar_animais, name='carregar_animais'),
    path('estoque/', views.estoque, name='estoque'),
    path('estoque/carregar/', views.carregar_estoque, name='carregar_estoque'),
    path('doenca/', views.doenca, name='doenca'),
    path('doenca/carregar/', views.carregar_doenca, name='carregar_doenca'),
    path('vinculardoenca/', views.vinculardoenca, name='vincular_doenca'),
    path('vinculardoenca/carregar/', views.carregar_vincular_doenca, name='carregar_vincular_doenca'),
    path('saida/', views.saida, name='saida'),
    path('saida/carregar/', views.carregar_saida, name='carregar_saida'),
]
