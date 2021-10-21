from django.db import models
from uuid import uuid4

class Entidade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cnpj = models.CharField(max_length=45, unique= True,null=True)
    nome = models.CharField(max_length=90)
    nome_fantasia = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique= True)
    created_at = models.DateTimeField(auto_now_add=True)

class Representante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE)
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45, unique=True)
    endereco = models.CharField(max_length=45)
    observacao = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_representante = models.ForeignKey(Representante, on_delete=models.CASCADE)
    papel = models.CharField(max_length=90)
    login = models.CharField(max_length=40)
    senha = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

class Familia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nomeChefeFamilia = models.CharField(max_length=45)
    cpfChefeFamilia = models.CharField(max_length=45, unique= True)
    endereco = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)

class IntegranteFamiliar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45, unique= True)
    created_at = models.DateTimeField(auto_now_add=True)

class Movimentos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    data = models.DateTimeField()
    justifica = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)

class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    descricao = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)

class Itens(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)

class MovimentoItens(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_movimento= models.ForeignKey(Movimentos, on_delete=models.CASCADE)
    id_itens = models.ForeignKey(Itens, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)