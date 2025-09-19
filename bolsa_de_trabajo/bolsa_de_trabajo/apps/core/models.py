from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)  # No se repite
    contrasena = models.CharField(max_length=100)  # más adelante se puede encriptar

    def __str__(self):
        return f"{self.nombre} ({self.correo})"

