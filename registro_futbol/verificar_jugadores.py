#!/usr/bin/env python
"""
Script para verificar jugadores existentes y sus imágenes
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'registro_futbol.settings')
django.setup()

from futbol.models import Jugador, Equipo, Pais
from django.conf import settings

def verificar_jugadores():
    """Verifica jugadores existentes y sus imágenes"""
    
    print("=== VERIFICACIÓN DE JUGADORES ===")
    print(f"Total de jugadores en la base de datos: {Jugador.objects.count()}")
    print("-" * 50)
    
    # Lista de jugadores que queremos verificar
    jugadores_objetivo = [
        "Edinson Cavani",
        "Enzo Pérez", 
        "Franco Armani",
        "Gerson",
        "Léo Pereira",
        "Paulo Díaz",
        "Pedro",
        "Raphael Veiga"
    ]
    
    # Verificar cada jugador objetivo
    for nombre in jugadores_objetivo:
        jugador = Jugador.objects.filter(nombre=nombre).first()
        if jugador:
            tiene_imagen = "✅ CON IMAGEN" if jugador.foto else "❌ SIN IMAGEN"
            print(f"{nombre}: {tiene_imagen}")
            if jugador.foto:
                print(f"  - Archivo: {jugador.foto.name}")
        else:
            print(f"{nombre}: ❌ NO EXISTE")
    
    print("-" * 50)
    
    # Mostrar todos los jugadores existentes
    print("TODOS LOS JUGADORES EXISTENTES:")
    for jugador in Jugador.objects.all().order_by('nombre'):
        tiene_imagen = "✅" if jugador.foto else "❌"
        print(f"{tiene_imagen} {jugador.nombre} ({jugador.equipo.nombre})")
    
    print("-" * 50)
    
    # Verificar archivos de imagen
    media_path = os.path.join(settings.MEDIA_ROOT, 'jugadores')
    print(f"ARCHIVOS EN {media_path}:")
    if os.path.exists(media_path):
        archivos = os.listdir(media_path)
        for archivo in sorted(archivos):
            if archivo.endswith('.jpeg'):
                print(f"  📁 {archivo}")
    else:
        print("  ❌ Carpeta no existe")

if __name__ == "__main__":
    verificar_jugadores() 