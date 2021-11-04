from django.db import models
from uuid import uuid4

class Entidade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cnpj = models.CharField(max_length=45, unique= True,null=True)
    nome_fantasia = models.CharField(max_length=45)
    nome_representante = models.CharField(max_length=90)
    cpf_representante = models.CharField(max_length=11, unique=True,null=True)
    endereco = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique= True)
    created_at = models.DateTimeField(auto_now_add=True)

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE)
    papel = models.CharField(max_length=90)
    login = models.CharField(max_length=40)
    senha = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

class Familia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nomeChefeFamilia = models.CharField(max_length=45)
    cpfChefeFamilia = models.CharField(max_length=45, unique= True)
    endereco = models.CharField(max_length=45)
    telefone1 = models.CharField(max_length=45)
    telefone2 = models.CharField(max_length=45, null=True)
    endereco = models.CharField(max_length=45)
    numeroDeDependentes = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class IntegranteFamiliar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45, unique= True)
    telefone = models.CharField(max_length=45, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Movimentos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    data = models.DateTimeField()
    justifica = models.CharField(max_length=90, null= True)
    created_at = models.DateTimeField(auto_now_add=True)

class MovimentoItens(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_movimento= models.ForeignKey(Movimentos, on_delete=models.CASCADE)
    nomeItem = models.CharField(max_length=45)
    quantidade = models.IntegerField()
    descricaoItem= models.CharField(max_length=95)
    created_at = models.DateTimeField(auto_now_add=True)