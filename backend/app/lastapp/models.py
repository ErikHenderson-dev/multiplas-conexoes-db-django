from django.db import models

# Create your models here.
# Create your models here.
class ContatoLast(models.Model):
    nome_2 = models.CharField(max_length=255)
    sobrenome_2 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nome_2

class ContatoLastOld(models.Model):
    nome_2 = models.CharField(max_length=255)
    sobrenome_2 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nome_2