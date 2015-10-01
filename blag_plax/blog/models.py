# Cada clase es una tabla en la base de datos, y cada campo, es una columna, aqui se definen con tipos de datos y todo.
from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('date published')


class Comentario(models.Model):
    texto = models.ForeignKey(Post) #En este campo se hace la relacion con la clase de arriba (Un comentario tiene un post) 1:1, relacion uno a uno
    votos = models.IntegerField(default=0)