from rest_framework import serializers
from api import models

class EntidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entidade
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Familia
        fields = '__all__'

class IntegranteFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IntegranteFamiliar
        fields = '__all__'

class MovimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movimentos
        fields = '__all__'

class MovimentoItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovimentoItens
        fields = '__all__'