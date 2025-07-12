#!/usr/bin/env python
"""
Script para agregar imágenes de jugadores específicos
Ejecutar desde la carpeta registro_futbol/
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

def agregar_jugadores_con_imagenes():
    """Agrega o actualiza jugadores con sus imágenes .jpeg"""
    
    # Obtener equipos existentes
    try:
        boca = Equipo.objects.get(nombre="Boca Juniors")
        river = Equipo.objects.get(nombre="River Plate")
        flamengo = Equipo.objects.get(nombre="Flamengo")
        palmeiras = Equipo.objects.get(nombre="Palmeiras")
    except Equipo.DoesNotExist as e:
        print(f"Error: {e}")
        print("Primero ejecuta: python manage.py cargar_datos")
        return
    
    # Obtener países existentes
    argentina = Pais.objects.get(nombre="Argentina")
    brasil = Pais.objects.get(nombre="Brasil")
    uruguay = Pais.objects.get(nombre="Uruguay")

    # Definir la ruta de las imágenes
    media_path = os.path.join(settings.MEDIA_ROOT, 'jugadores')
    
    # Crear el directorio si no existe
    os.makedirs(media_path, exist_ok=True)

    # Lista de jugadores con sus imágenes
    jugadores_con_imagenes = [
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

    print("Iniciando proceso de agregar jugadores con imágenes...")
    print(f"Buscando imágenes en: {media_path}")
    print("-" * 50)

    for jugador_data in jugadores_con_imagenes:
        # Verificar si el jugador ya existe
        jugador_existente = Jugador.objects.filter(nombre=jugador_data["nombre"]).first()
        
        if jugador_existente:
            # Actualizar jugador existente
            jugador_existente.edad = jugador_data["edad"]
            jugador_existente.posicion = jugador_data["posicion"]
            jugador_existente.equipo = jugador_data["equipo"]
            jugador_existente.pais = jugador_data["pais"]
            
            # Agregar imagen si existe el archivo
            imagen_path = os.path.join(media_path, jugador_data["imagen"])
            if os.path.exists(imagen_path):
                with open(imagen_path, 'rb') as img_file:
                    jugador_existente.foto.save(
                        jugador_data["imagen"],
                        File(img_file),
                        save=False
                    )
                print(f"✅ Jugador actualizado con imagen: {jugador_data['nombre']}")
            else:
                print(f"⚠️  Jugador actualizado sin imagen (archivo no encontrado): {jugador_data['nombre']} - {jugador_data['imagen']}")
            
            jugador_existente.save()
        else:
            # Crear nuevo jugador
            jugador = Jugador.objects.create(
                nombre=jugador_data["nombre"],
                edad=jugador_data["edad"],
                posicion=jugador_data["posicion"],
                equipo=jugador_data["equipo"],
                pais=jugador_data["pais"]
            )
            
            # Agregar imagen si existe el archivo
            imagen_path = os.path.join(media_path, jugador_data["imagen"])
            if os.path.exists(imagen_path):
                with open(imagen_path, 'rb') as img_file:
                    jugador.foto.save(
                        jugador_data["imagen"],
                        File(img_file),
                        save=False
                    )
                jugador.save()
                print(f"✅ Jugador creado con imagen: {jugador_data['nombre']}")
            else:
                print(f"⚠️  Jugador creado sin imagen (archivo no encontrado): {jugador_data['nombre']} - {jugador_data['imagen']}")

    print("-" * 50)
    print("Proceso completado!")
    print(f"Total de jugadores en la base de datos: {Jugador.objects.count()}")

if __name__ == "__main__":
    agregar_jugadores_con_imagenes() 