from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pais, Equipo, Torneo, Jugador, Partido
from .serializers import (
    PaisSerializer, PaisDetalleSerializer, EquipoSerializer, 
    TorneoSerializer, JugadorSerializer, PartidoSerializer
)

class JugadorListView(generics.ListAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class EquipoListView(generics.ListAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class TorneoListView(generics.ListAPIView):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer

class PartidoListView(generics.ListAPIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

class JugadorDetailView(generics.RetrieveAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class EquipoDetailView(generics.RetrieveAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class PaisDetailView(generics.RetrieveAPIView):
    queryset = Pais.objects.all()
    serializer_class = PaisDetalleSerializer