# Generated by Django 2.0.3 on 2018-05-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao_Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_solicitacao', models.DateField(verbose_name='data_solicitacao')),
                ('status_sm', models.CharField(max_length=20, verbose_name='status_sm')),
            ],
        ),
    ]
