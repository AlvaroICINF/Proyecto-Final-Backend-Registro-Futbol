#!/usr/bin/env python
"""
Script para agregar equipos chilenos y actualizar escudos de todos los equipos
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'registro_futbol.settings')
django.setup()

from django.core.files import File
from futbol.models import Equipo, Pais
from django.conf import settings

def agregar_equipos_chilenos_y_actualizar_escudos():
    # 1. Asegurar que el país Chile existe
    chile, _ = Pais.objects.get_or_create(nombre="Chile")

    # 2. Datos de los equipos chilenos
    equipos_chilenos = [
        {
            "nombre": "Colo Colo",
            "entrenador": "Jorge Almirón",
            "escudo": "colocolo.png",
            "pais": chile
        },
        {
            "nombre": "Universidad de Chile",
            "entrenador": "Gustavo Álvarez",
            "escudo": "UdeChile.png",
            "pais": chile
        },
        {
            "nombre": "Universidad Católica",
            "entrenador": "Daniel Garnero",
            "escudo": "UCatolica.png",
            "pais": chile
        }
    ]

    # 3. Agregar o actualizar equipos chilenos
    media_escudos = os.path.join(settings.MEDIA_ROOT, 'escudos')
    print(f"Buscando escudos en: {media_escudos}")
    for equipo_data in equipos_chilenos:
        equipo, created = Equipo.objects.get_or_create(
            nombre=equipo_data["nombre"],
            defaults={
                "entrenador": equipo_data["entrenador"],
                "pais": equipo_data["pais"]
            }
        )
        equipo.entrenador = equipo_data["entrenador"]
        equipo.pais = equipo_data["pais"]
        # Asignar escudo si existe el archivo
        escudo_path = os.path.join(media_escudos, equipo_data["escudo"])
        if os.path.exists(escudo_path):
            with open(escudo_path, 'rb') as img_file:
                equipo.escudo.save(equipo_data["escudo"], File(img_file), save=False)
            print(f"✅ {equipo.nombre}: Escudo asignado ({equipo_data['escudo']})")
        else:
            print(f"⚠️  {equipo.nombre}: Escudo no encontrado ({equipo_data['escudo']})")
        equipo.save()
        print(f"{'Creado' if created else 'Actualizado'} equipo: {equipo.nombre}")

    # 4. Actualizar escudos de todos los equipos existentes si el archivo existe
    print("\nActualizando escudos de todos los equipos existentes...")
    for equipo in Equipo.objects.all():
        nombre_archivo = equipo.nombre.lower().replace(' ', '') + '.png'
        escudo_path = os.path.join(media_escudos, nombre_archivo)
        if os.path.exists(escudo_path):
            with open(escudo_path, 'rb') as img_file:
                equipo.escudo.save(nombre_archivo, File(img_file), save=False)
            equipo.save()
            print(f"✅ {equipo.nombre}: Escudo actualizado ({nombre_archivo})")
        else:
            print(f"{equipo.nombre}: No se encontró escudo ({nombre_archivo})")

    print("\nProceso completado!")

if __name__ == "__main__":
    agregar_equipos_chilenos_y_actualizar_escudos() 