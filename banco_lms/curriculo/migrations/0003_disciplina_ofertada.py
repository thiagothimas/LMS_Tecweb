# Generated by Django 2.0.3 on 2018-05-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0002_disciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina_Ofertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio_matricula', models.DateField(verbose_name='data_inicio_matricula')),
                ('data_fim_matricula', models.DateField(verbose_name='data_fim_matricula')),
                ('ano', models.IntegerField(verbose_name='ano')),
                ('semestre', models.CharField(max_length=1, verbose_name='semestre')),
                ('turma', models.CharField(max_length=2, verbose_name='turma')),
                ('metodologia', models.CharField(max_length=3000, verbose_name='metodologia')),
                ('recursos', models.CharField(max_length=3000, verbose_name='recursos')),
                ('criterio_avaliacao', models.CharField(max_length=3000, verbose_name='criterio_avaliacao')),
                ('plano_aulas', models.CharField(max_length=10000, verbose_name='plano_aulas')),
            ],
        ),
    ]
