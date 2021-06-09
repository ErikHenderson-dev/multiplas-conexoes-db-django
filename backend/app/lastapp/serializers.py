from rest_framework import serializers
from .models import ContatoLastNome

class LastappContatoNomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoLastNome
        fields = '__all__'
