#!/usr/bin/env python
"""
Script para forzar la actualización de imágenes de jugadores específicos
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'registro_futbol.settings')
django.setup()

from django.core.files import File
from futbol.models import Jugador, Equipo, Pais
from django.conf import settings

def forzar_actualizacion_imagenes():
    """Fuerza la actualización de imágenes para jugadores específicos"""
    
    # Obtener equipos existentes
    boca = Equipo.objects.get(nombre="Boca Juniors")
    river = Equipo.objects.get(nombre="River Plate")
    flamengo = Equipo.objects.get(nombre="Flamengo")
    palmeiras = Equipo.objects.get(nombre="Palmeiras")
    
    # Obtener países existentes
    argentina = Pais.objects.get(nombre="Argentina")
    brasil = Pais.objects.get(nombre="Brasil")
    uruguay = Pais.objects.get(nombre="Uruguay")

    # Definir la ruta de las imágenes
    media_path = os.path.join(settings.MEDIA_ROOT, 'jugadores')
    
    # Lista específica de jugadores con sus imágenes
    jugadores_imagenes = [
        {
            "nombre": "Edinson Cavani",
            "edad": 36,
            "posicion": "Delantero",
            "equipo": boca,
            "pais": uruguay,
            "imagen": "edinsoncavani.jpeg"
        },
        {
            "nombre": "Enzo Pérez",
            "edad": 37,
            "posicion": "Mediocampista",
            "equipo": river,
            "pais": argentina,
            "imagen": "enzoperez.jpeg"
        },
        {
            "nombre": "Franco Armani",
            "edad": 37,
            "posicion": "Arquero",
            "equipo": river,
            "pais": argentina,
            "imagen": "francoarmani.jpeg"
        },
        {
            "nombre": "Gerson",
            "edad": 26,
            "posicion": "Mediocampista",
            "equipo": flamengo,
            "pais": brasil,
            "imagen": "gerson.jpeg"
        },
        {
            "nombre": "Léo Pereira",
            "edad": 27,
            "posicion": "Defensor",
            "equipo": flamengo,
            "pais": brasil,
            "imagen": "leopereira.jpeg"
        },
        {
            "nombre": "Paulo Díaz",
            "edad": 29,
            "posicion": "Defensor",
            "equipo": river,
            "pais": argentina,
            "imagen": "paulodiaz.jpeg"
        },
        {
            "nombre": "Pedro",
            "edad": 26,
            "posicion": "Delantero",
            "equipo": flamengo,
            "pais": brasil,
            "imagen": "pedro.jpeg"
        },
        {
            "nombre": "Raphael Veiga",
            "edad": 28,
            "posicion": "Mediocampista",
            "equipo": palmeiras,
            "pais": brasil,
            "imagen": "raphaelveiga.jpeg"
        }
    ]

    print("=== FORZANDO ACTUALIZACIÓN DE IMÁGENES ===")
    print(f"Buscando imágenes en: {media_path}")
    print("-" * 60)

    for jugador_data in jugadores_imagenes:
        # Buscar o crear jugador
        jugador, created = Jugador.objects.get_or_create(
            nombre=jugador_data["nombre"],
            defaults={
                "edad": jugador_data["edad"],
                "posicion": jugador_data["posicion"],
                "equipo": jugador_data["equipo"],
                "pais": jugador_data["pais"]
            }
        )
        
        # Actualizar datos del jugador
        jugador.edad = jugador_data["edad"]
        jugador.posicion = jugador_data["posicion"]
        jugador.equipo = jugador_data["equipo"]
        jugador.pais = jugador_data["pais"]
        
        # Verificar y agregar imagen
        imagen_path = os.path.join(media_path, jugador_data["imagen"])
        if os.path.exists(imagen_path):
            try:
                with open(imagen_path, 'rb') as img_file:
                    jugador.foto.save(
                        jugador_data["imagen"],
                        File(img_file),
                        save=False
                    )
                jugador.save()
                status = "CREADO" if created else "ACTUALIZADO"
                print(f"✅ {jugador_data['nombre']}: {status} con imagen")
            except Exception as e:
                print(f"❌ Error con {jugador_data['nombre']}: {e}")
        else:
            jugador.save()
            print(f"⚠️  {jugador_data['nombre']}: {'CREADO' if created else 'ACTUALIZADO'} sin imagen (archivo no encontrado: {jugador_data['imagen']})")

    print("-" * 60)
    print("Proceso completado!")
    print(f"Total de jugadores en la base de datos: {Jugador.objects.count()}")

if __name__ == "__main__":
    forzar_actualizacion_imagenes() 