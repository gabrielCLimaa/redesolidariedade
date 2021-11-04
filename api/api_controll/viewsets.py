from rest_framework import viewsets
from api.api_controll import serializers
from api import models

class EntidadeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EntidadeSerializer
    queryset = models.Entidade.objects.all()

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsuarioSerializer
    queryset = models.Usuario.objects.all()

class FamiliaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FamiliaSerializer
    queryset = models.Familia.objects.all()

class IntegranteFamiliarViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IntegranteFamiliarSerializer
    queryset = models.IntegranteFamiliar.objects.all()

class MovimentosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MovimentosSerializer
    queryset = models.Movimentos.objects.all()

class MovimentoItensViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MovimentoItensSerializer
    queryset = models.MovimentoItens.objects.all()







