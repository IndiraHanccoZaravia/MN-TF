from django.urls import path
from . import views
from django.contrib import admin
from calculadora.views import *

urlpatterns = [
    path('', index.as_view(), name = ''),
    path('tema', tema.as_view(), name = 'tema'),
    path('curso', curso.as_view(), name = 'curso'),
    path('indice', indice.as_view(), name = 'indice'),
    path('biseccion', biseccion.as_view(), name = 'biseccion'),
    path('falsaposicion', falsaposicion.as_view(), name = 'falsaposicion'),
    path('puntofijo', puntofijo.as_view(), name = 'puntofijo'),
    path('secante', secante.as_view(), name = 'secante'),
    path('newton', newton.as_view(), name = 'newton'),
    path('muller', muller.as_view(), name = 'muller'),
    path('bairstow', bairstow.as_view(), name = 'bairstow'),
]