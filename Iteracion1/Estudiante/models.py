from django.db import models
import uuid

# Create your models here.
class Estudiante(models.Model):

    id        = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_Equipo = models.ForeignKey('Equipo.Equipo', on_delete=models.CASCADE, blank=False, null=False)
    historial = models.CharField(max_length=2000) #falta definirlo bien, debería guardarse una lista de equipos, pero solo debo ingresar uno.
    Presentó  = models.BooleanField(default=False)
    Nombre    = models.CharField(max_length=50, default="")
    Notas     = models.FloatField(default=1.0)
    class Meta:
        unique_together = [['id', 'id_Equipo']]