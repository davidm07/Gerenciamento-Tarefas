from django.db import models

# Create your models here.
class Task(models.Model):
    titulo = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class User(models.Model):
    usuario = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.usuario