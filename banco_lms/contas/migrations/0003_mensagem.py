# Generated by Django 2.0.3 on 2018-05-09 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_aluno_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=400, verbose_name='assunto')),
                ('referencia', models.CharField(max_length=400, verbose_name='referencia')),
                ('conteudo', models.CharField(max_length=400, verbose_name='conteudo')),
                ('status', models.CharField(max_length=30, verbose_name='status')),
                ('data_envio', models.DateField(verbose_name='data_envio')),
                ('data_resposta', models.DateField(verbose_name='data_resposta')),
                ('resposta', models.CharField(max_length=400, verbose_name='resposta')),
            ],
        ),
    ]