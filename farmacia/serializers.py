from rest_framework import serializers
from .models import Medicament, Client

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
