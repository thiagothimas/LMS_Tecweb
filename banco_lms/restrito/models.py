<--!Models-->
from django.db import models
  
class Solicitacao_Matricula(models.Model):
    
    data_solicitacao = models.DateField("data_solicitacao")
    status_sm = models.CharField("status_sm", max_length=15)

    def __str__(self):
        return self.nome

		
class Atividade(models.Model):

    titulo = models.IntegerField("titulo")
    descricao = models.CharField("descricao", max_length=3000)
    conteudo = models.CharField("conteudo", max_length=3000)
    tipo = models.CharField("tipo", max_length=50)
	
    def __str__(self):
        return self.nome

		
class Atividade_Vinculada(models.Model):

    rotulo = models.CharField("rotulo", max_length=3)
    status_av = models.CharField("status_av", max_length=15)
    Data_InicioRespostas = models.DateField("Data_InicioRespostas")
    Data_FimRespostas = models.DateField("Data_FimRespostas")

    def __str__(self):
        return self.nome
		
class Entrega(models.Model):

    titulo = models.CharField("titulo", max_length=20)
    resposta = models.CharField("resposta", max_length=3000)
    data_entrega = models.DateField("data_entrega")
    status_e = models.CharField("status_e", max_length=40)
    nota = models.DecimalField("nota", decimal_places=2, max_digits=2)
    dt_avaliacao = models.DateField("dt_avaliacao")
    obs = models.CharField("obs", max_length=3000)

    def __str__(self):
        return self.nome
