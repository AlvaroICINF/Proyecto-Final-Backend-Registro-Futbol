from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Países"

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    entrenador = models.CharField(max_length=100)
    escudo = models.ImageField(upload_to='escudos/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class EquipoTorneo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('equipo', 'torneo')

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='jugadores/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Partido(models.Model):
    fecha = models.DateField()
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    goles_local = models.IntegerField(default=0)
    goles_visitante = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} - {self.fecha}"