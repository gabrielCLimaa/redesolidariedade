# Generated by Django 3.2.8 on 2021-10-21 16:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=90)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entidade',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cnpj', models.CharField(max_length=45, unique=True)),
                ('nome', models.CharField(max_length=90)),
                ('nome_fantasia', models.CharField(max_length=45)),
                ('endereco', models.CharField(max_length=45)),
                ('telefone', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nomeChefeFamilia', models.CharField(max_length=45)),
                ('cpfChefeFamilia', models.CharField(max_length=45)),
                ('endereco', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Itens',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('cpf', models.CharField(max_length=45)),
                ('endereco', models.CharField(max_length=45)),
                ('observacao', models.CharField(max_length=90)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_entidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.entidade')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('papel', models.CharField(max_length=90)),
                ('login', models.CharField(max_length=40)),
                ('senha', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_representante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.representante')),
            ],
        ),
        migrations.CreateModel(
            name='Movimentos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data', models.DateTimeField()),
                ('justifica', models.CharField(max_length=90)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.familia')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='MovimentoItens',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_itens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.itens')),
                ('id_movimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.movimentos')),
            ],
        ),
        migrations.CreateModel(
            name='IntegranteFamiliar',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('cpf', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.familia')),
            ],
        ),
    ]
