from django.db import models
from django.utils import timezone

class categoria(models.Model):
    nombre=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class confesiones(models.Model):
    Nombre_confesion = models.CharField(max_length=200)
    contenido = models.TextField()
    tag=models.ForeignKey(categoria)
    created_date = models.DateTimeField(
            default=timezone.now())

    def __str__(self):
        return self.Nombre_confesion

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def elimnar(self):
        self.delete()
