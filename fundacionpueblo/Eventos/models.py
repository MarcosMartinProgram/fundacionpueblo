from django.db import models
import os 

# Create your models here.

class Eventos(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=150)
    imagen=models.ImageField(upload_to='eventos')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Evento' 
        verbose_name_plural='Eventos'

    def __str__(self):
        return self.titulo