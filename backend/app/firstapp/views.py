from rest_framework import viewsets
from . import serializers
from .models import ContatoFirst

class Contatos(viewsets.ModelViewSet):
   serializer_class = serializers.FirstappContatosSerializer
   queryset = ContatoFirst.objects.all()



