# Instrucciones para Agregar Imágenes de Jugadores

## Pasos para agregar las imágenes de los jugadores:

### 1. Preparar las imágenes
Coloca las siguientes imágenes .jpeg en la carpeta `registro_futbol/media/jugadores/`:

- `edinsoncavani.jpeg`
- `enzoperez.jpeg`
- `francoarmani.jpeg`
- `gerson.jpeg`
- `leopereira.jpeg`
- `paulodiaz.jpeg`
- `pedro.jpeg`
- `raphaelveiga.jpeg`

### 2. Crear la carpeta de imágenes
Si la carpeta no existe, créala:
```bash
mkdir -p registro_futbol/media/jugadores
```

### 3. Ejecutar el comando (Opción 1 - Comando Django)
```bash
cd registro_futbol
python manage.py agregar_jugadores_imagenes
```

### 3. Ejecutar el script (Opción 2 - Script independiente)
```bash
cd registro_futbol
python agregar_imagenes_jugadores.py
```

### 4. Verificar el resultado
El comando te mostrará:
- ✅ Jugadores creados/actualizados con imagen
- ⚠️ Jugadores creados sin imagen (si no encuentra el archivo)

## Jugadores que se agregarán/actualizarán:

| Jugador | Equipo | Posición | Imagen |
|---------|--------|----------|--------|
| Edinson Cavani | Boca Juniors | Delantero | edinsoncavani.jpeg |
| Enzo Pérez | River Plate | Mediocampista | enzoperez.jpeg |
| Franco Armani | River Plate | Arquero | francoarmani.jpeg |
| Gerson | Flamengo | Mediocampista | gerson.jpeg |
| Léo Pereira | Flamengo | Defensor | leopereira.jpeg |
| Paulo Díaz | River Plate | Defensor | paulodiaz.jpeg |
| Pedro | Flamengo | Delantero | pedro.jpeg |
| Raphael Veiga | Palmeiras | Mediocampista | raphaelveiga.jpeg |

## Notas importantes:

- Las imágenes deben estar en formato .jpeg
- Los nombres de archivo deben coincidir exactamente con los especificados
- Si un jugador ya existe, se actualizará con la nueva imagen
- Si no encuentra una imagen, el jugador se creará sin foto
- Las imágenes se guardarán en la carpeta `media/jugadores/` del proyecto
- **Requisito previo**: Ejecutar `python manage.py cargar_datos` para crear equipos y países

## Ejemplo de uso completo:

```bash
# 1. Cargar datos base (si no lo has hecho)
cd registro_futbol
python manage.py cargar_datos

# 2. Colocar las imágenes en media/jugadores/

# 3. Ejecutar el script
python agregar_imagenes_jugadores.py

# 4. Verificar en el navegador
python manage.py runserver
# Ir a http://localhost:8000/jugadores/
``` 