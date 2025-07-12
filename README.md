# Registro de Fútbol - Django Backend

Sistema de gestión de jugadores, equipos, torneos y partidos de fútbol con API REST.

## Características

- CRUD completo para jugadores y equipos
- API REST con Django REST Framework
- Soporte para imágenes (fotos de jugadores y escudos de equipos)
- Interfaz administrativa
- Base de datos relacional completa

## Instalación

1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno: `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows)
4. Instalar dependencias: `pip install -r requirements.txt`
5. Ejecutar migraciones: `python manage.py migrate`
6. Crear superusuario: `python manage.py createsuperuser`
7. Cargar datos de prueba: `python manage.py loaddata fixtures/datos_prueba.json`
8. Ejecutar servidor: `python manage.py runserver`

## Endpoints de la API

### Listas
- `GET /api/jugadores/` - Lista de jugadores
- `GET /api/equipos/` - Lista de equipos con jugadores
- `GET /api/torneos/` - Lista de torneos con equipos participantes
- `GET /api/partidos/` - Lista de partidos
- `GET /api/paises/<id>/` - País específico con equipos, jugadores y torneos

### Detalles
- `GET /api/jugadores/<id>/` - Detalle de jugador
- `GET /api/equipos/<id>/` - Detalle de equipo con jugadores

## Uso

1. Acceder a la interfaz web en `http://localhost:8000`
2. Usar el admin en `http://localhost:8000/admin/`
3. Probar la API en `http://localhost:8000/api/`

## Estructura del Proyecto

registro_futbol/
├── futbol/
│   ├── migrations/
│   ├── templates/futbol/
│   ├── models.py
│   ├── views.py
│   ├── api_views.py
│   ├── serializers.py
│   ├── forms.py
│   ├── urls.py
│   └── api_urls.py
├── media/
│   ├── escudos/
│   └── jugadores/
├── manage.py
└── requirements.txt