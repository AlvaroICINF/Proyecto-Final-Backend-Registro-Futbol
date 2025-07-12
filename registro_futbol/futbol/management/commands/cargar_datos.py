from django.core.management.base import BaseCommand
from futbol.models import Pais, Equipo, Torneo, EquipoTorneo, Jugador, Partido
from datetime import date


#Se le pide a la IA que genere datos de prueba para la base de datos para mayor rapidez y eficacia.

class Command(BaseCommand):
    help = 'Carga datos de prueba en la base de datos'

    def handle(self, *args, **options):
        # Limpiar datos existentes
        Partido.objects.all().delete()
        EquipoTorneo.objects.all().delete()
        Jugador.objects.all().delete()
        Torneo.objects.all().delete()
        Equipo.objects.all().delete()
        Pais.objects.all().delete()

        # Crear países
        argentina = Pais.objects.create(nombre="Argentina")
        brasil = Pais.objects.create(nombre="Brasil")
        colombia = Pais.objects.create(nombre="Colombia")
        uruguay = Pais.objects.create(nombre="Uruguay")

        self.stdout.write(self.style.SUCCESS('Países creados'))

        # Crear equipos
        boca = Equipo.objects.create(
            nombre="Boca Juniors",
            pais=argentina,
            entrenador="Jorge Almirón"
        )
        river = Equipo.objects.create(
            nombre="River Plate",
            pais=argentina,
            entrenador="Martín Demichelis"
        )
        flamengo = Equipo.objects.create(
            nombre="Flamengo",
            pais=brasil,
            entrenador="Tite"
        )
        palmeiras = Equipo.objects.create(
            nombre="Palmeiras",
            pais=brasil,
            entrenador="Abel Ferreira"
        )
        nacional = Equipo.objects.create(
            nombre="Nacional",
            pais=colombia,
            entrenador="Efraín Juárez"
        )
        penarol = Equipo.objects.create(
            nombre="Peñarol",
            pais=uruguay,
            entrenador="Mauricio Larriera"
        )

        self.stdout.write(self.style.SUCCESS('Equipos creados'))

        # Crear torneos
        copa_libertadores = Torneo.objects.create(
            nombre="Copa Libertadores",
            pais=argentina  # Puede ser cualquier país
        )
        copa_argentina = Torneo.objects.create(
            nombre="Copa Argentina",
            pais=argentina
        )
        brasileirao = Torneo.objects.create(
            nombre="Brasileirao",
            pais=brasil
        )

        self.stdout.write(self.style.SUCCESS('Torneos creados'))

        # Asociar equipos a torneos
        EquipoTorneo.objects.create(equipo=boca, torneo=copa_libertadores)
        EquipoTorneo.objects.create(equipo=river, torneo=copa_libertadores)
        EquipoTorneo.objects.create(equipo=flamengo, torneo=copa_libertadores)
        EquipoTorneo.objects.create(equipo=palmeiras, torneo=copa_libertadores)
        EquipoTorneo.objects.create(equipo=boca, torneo=copa_argentina)
        EquipoTorneo.objects.create(equipo=river, torneo=copa_argentina)
        EquipoTorneo.objects.create(equipo=flamengo, torneo=brasileirao)
        EquipoTorneo.objects.create(equipo=palmeiras, torneo=brasileirao)

        self.stdout.write(self.style.SUCCESS('Asociaciones equipo-torneo creadas'))

        # Crear jugadores
        jugadores_data = [
            # Boca Juniors
            {"nombre": "Sergio Romero", "edad": 36, "posicion": "Arquero", "equipo": boca, "pais": argentina},
            {"nombre": "Marcos Rojo", "edad": 33, "posicion": "Defensor", "equipo": boca, "pais": argentina},
            {"nombre": "Pol Fernández", "edad": 31, "posicion": "Mediocampista", "equipo": boca, "pais": argentina},
            {"nombre": "Edinson Cavani", "edad": 36, "posicion": "Delantero", "equipo": boca, "pais": uruguay},
            
            # River Plate
            {"nombre": "Franco Armani", "edad": 37, "posicion": "Arquero", "equipo": river, "pais": argentina},
            {"nombre": "Paulo Díaz", "edad": 29, "posicion": "Defensor", "equipo": river, "pais": argentina},
            {"nombre": "Enzo Pérez", "edad": 37, "posicion": "Mediocampista", "equipo": river, "pais": argentina},
            {"nombre": "Miguel Borja", "edad": 30, "posicion": "Delantero", "equipo": river, "pais": colombia},
            
            # Flamengo
            {"nombre": "Rossi", "edad": 25, "posicion": "Arquero", "equipo": flamengo, "pais": brasil},
            {"nombre": "Léo Pereira", "edad": 27, "posicion": "Defensor", "equipo": flamengo, "pais": brasil},
            {"nombre": "Gerson", "edad": 26, "posicion": "Mediocampista", "equipo": flamengo, "pais": brasil},
            {"nombre": "Pedro", "edad": 26, "posicion": "Delantero", "equipo": flamengo, "pais": brasil},
            
            # Palmeiras
            {"nombre": "Weverton", "edad": 35, "posicion": "Arquero", "equipo": palmeiras, "pais": brasil},
            {"nombre": "Gustavo Gómez", "edad": 30, "posicion": "Defensor", "equipo": palmeiras, "pais": brasil},
            {"nombre": "Raphael Veiga", "edad": 28, "posicion": "Mediocampista", "equipo": palmeiras, "pais": brasil},
            {"nombre": "Endrick", "edad": 17, "posicion": "Delantero", "equipo": palmeiras, "pais": brasil},
        ]

        for jugador_data in jugadores_data:
            Jugador.objects.create(**jugador_data)

        self.stdout.write(self.style.SUCCESS('Jugadores creados'))

        # Crear partidos
        partidos_data = [
            {
                "fecha": date(2024, 3, 15),
                "equipo_local": boca,
                "equipo_visitante": river,
                "torneo": copa_argentina,
                "goles_local": 2,
                "goles_visitante": 1
            },
            {
                "fecha": date(2024, 3, 20),
                "equipo_local": flamengo,
                "equipo_visitante": palmeiras,
                "torneo": brasileirao,
                "goles_local": 3,
                "goles_visitante": 2
            },
            {
                "fecha": date(2024, 4, 10),
                "equipo_local": boca,
                "equipo_visitante": flamengo,
                "torneo": copa_libertadores,
                "goles_local": 1,
                "goles_visitante": 0
            },
        ]

        for partido_data in partidos_data:
            Partido.objects.create(**partido_data)

        self.stdout.write(self.style.SUCCESS('Partidos creados'))
        self.stdout.write(self.style.SUCCESS('Datos de prueba cargados exitosamente'))