from django.core.management.base import BaseCommand
from django.core.files import File
from futbol.models import Jugador, Equipo, Pais
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Agrega jugadores específicos con imágenes .jpeg'

    def handle(self, *args, **options):
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
                
                jugador_existente.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Jugador actualizado: {jugador_data["nombre"]}')
                )
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
                    self.stdout.write(
                        self.style.SUCCESS(f'Jugador creado con imagen: {jugador_data["nombre"]}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Jugador creado sin imagen (archivo no encontrado): {jugador_data["nombre"]} - {jugador_data["imagen"]}')
                    )

        self.stdout.write(self.style.SUCCESS('Proceso completado')) 