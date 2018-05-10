from django.db import models

class Coordenador(models.Model):

	login = models.CharField("login", max_length=100)
	senha = models.CharField("senha", max_length=30)
	nome = models.CharField("nome", max_length=100)
	email = models.EmailField("email", max_length=200)
	celular = models.IntegerField("celular")
	data_expiracao = models.DateField("data_expiracao")
    
	def __str__(self):
		return self.nome
		
class Aluno(models.Model):
    
    login = models.CharField("login", max_length=100)
    senha = models.CharField("senha", max_length=30)
    nome = models.CharField("nome", max_length=100)
    email = models.EmailField("email", max_length=200)
    celular = models.IntegerField("celular")
    data_expiracao = models.DateField("data_expiracao")
    ra = models.IntegerField("ra")

    def __str__(self):
        return self.nome

class Professor(models.Model):
    
    login = models.CharField("login", max_length=100)
    senha = models.CharField("senha", max_length=30)
    nome = models.CharField("nome", max_length=100)
    email = models.EmailField("email", max_length=200)
    celular = models.CharField("celular", max_length=50)
    data_expiracao = models.DateField("data_expiracao", max_length=100)
    apelido = models.CharField("apelido", max_length=50)

    def __str__(self):
        return self.nome
		
class Mensagem(models.Model):

    assunto = models.CharField("assunto", max_length=400)
    referencia = models.CharField("referencia", max_length=400)
    conteudo = models.CharField("conteudo", max_length=400)
    status = models.CharField("status", max_length=30)
    data_envio = models.DateField("data_envio")
    data_resposta = models.DateField("data_resposta")
    resposta = models.CharField("resposta", max_length=400)

    def __str__(self):
        return self.nome    
