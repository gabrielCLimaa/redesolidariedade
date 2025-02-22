# Generated by Django 3.2.8 on 2021-11-04 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_movimentoitens_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entidade',
            old_name='nome',
            new_name='nome_representante',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id_representante',
        ),
        migrations.AddField(
            model_name='entidade',
            name='cpf_representante',
            field=models.CharField(max_length=11, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_entidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.entidade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movimentos',
            name='justifica',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.DeleteModel(
            name='Representante',
        ),
    ]
