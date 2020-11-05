from django.db import models

from django.contrib.auth.models import User #importar usuario

# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)    #cambia cuando se crea
    fm = models.DateTimeField(auto_now=True)    #cambia cuando se crea o modifica
    uc = models.ForeignKey(User, on_delete=models.CASCADE)         #usuario que crea
    um = models.IntegerField(blank=True,null=True)    #usuario modifica

    class Meta:
        abstract=True     #Este modelo no lo toma en cuanta a la hora de procesar un migracion

