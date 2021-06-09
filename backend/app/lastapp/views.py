from rest_framework import viewsets
from . import serializers
from .models import ContatoLastNome

class ContatosNome(viewsets.ModelViewSet):
   serializer_class = serializers.LastappContatoNomeSerializer
   queryset = ContatoLastNome.objects.all()


