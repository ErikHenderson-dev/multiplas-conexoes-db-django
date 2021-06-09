from rest_framework import serializers
from .models import ContatoFirst

class FirstappContatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoFirst
        fields = '__all__'