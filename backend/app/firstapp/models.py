from django.db import models

# Create your models here.
class ContatoFirst(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nome