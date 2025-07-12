from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Jugador, Equipo
from .forms import JugadorForm, EquipoForm
# Create your views here.

def index(request):
    return render(request, 'futbol/index.html')

def jugador_lista(request):
    jugadores = Jugador.objects.all()
    return render(request, 'futbol/jugador_lista.html', {'jugadores': jugadores})

def jugador_detalle(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    return render(request, 'futbol/jugador_detalle.html', {'jugador': jugador})

def jugador_crear(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Jugador creado exitosamente')
            return redirect('jugador_lista')
    else:
        form = JugadorForm()
    return render(request, 'futbol/jugador_form.html', {'form': form, 'titulo': 'Crear Jugador'})

def jugador_editar(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES, instance=jugador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Jugador actualizado exitosamente')
            return redirect('jugador_lista')
    else:
        form = JugadorForm(instance=jugador)
    return render(request, 'futbol/jugador_form.html', {'form': form, 'titulo': 'Editar Jugador'})

def jugador_eliminar(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    if request.method == 'POST':
        jugador.delete()
        messages.success(request, 'Jugador eliminado exitosamente')
        return redirect('jugador_lista')
    return render(request, 'futbol/jugador_confirmar_eliminar.html', {'jugador': jugador})


def equipo_lista(request):
    equipos = Equipo.objects.all()
    return render(request, 'futbol/equipo_lista.html', {'equipos': equipos})

def equipo_detalle(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    jugadores = equipo.jugador_set.all()
    return render(request, 'futbol/equipo_detalle.html', {'equipo': equipo, 'jugadores': jugadores})

def equipo_crear(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipo creado exitosamente')
            return redirect('equipo_lista')
    else:
        form = EquipoForm()
    return render(request, 'futbol/equipo_form.html', {'form': form, 'titulo': 'Crear Equipo'})

def equipo_editar(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipo actualizado exitosamente')
            return redirect('equipo_lista')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'futbol/equipo_form.html', {'form': form, 'titulo': 'Editar Equipo'})

def equipo_eliminar(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        equipo.delete()
        messages.success(request, 'Equipo eliminado exitosamente')
        return redirect('equipo_lista')
    return render(request, 'futbol/equipo_confirmar_eliminar.html', {'equipo': equipo})