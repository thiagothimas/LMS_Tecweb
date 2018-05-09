from django.db import models

class Curso(models.Model):
    
    nome = models.CharField("nome", max_length=100)

    def __str__(self):
        return self.nome
		
class Disciplina(models.Model):
    
    nome = models.CharField("nome", max_length=60)
    data_expiracao = models.DateField("data_expiracao")
    status = models.CharField("status", max_length=10)
    plano_ensino = models.CharField("plano_ensino",max_length=3000)
    carga_horaria = models.IntegerField("carga_horaria")
    competencias = models.CharField("competencias",max_length=3000)
    habilidade = models.CharField("habilidade",max_length=3000)
    ementa = models.CharField("ementa",max_length=3000)
    conteudo_programatico = models.CharField("conteudo_programatico",max_length=3000)
    bibliografia_basica = models.CharField("bibliografia_basica",max_length=3000)
    bibliografia_complementar = models.CharField("bibliografia_complementar",max_length=3000)
    percentual_pratico = models.IntegerField("percentual_pratico")
    percentual_teorico = models.IntegerField("percentual_teorico")

    def __str__(self):
        return self.nome
		
class Disciplina_Ofertada(models.Model):
    
    data_inicio_matricula = models.DateField("data_inicio_matricula")
    data_fim_matricula = models.DateField("data_fim_matricula")
    ano = models.IntegerField("ano")
    semestre = models.CharField ("semestre",max_length=1)
    turma = models.CharField ("turma",max_length=2)
    metodologia = models.CharField("metodologia",max_length=3000)
    recursos = models.CharField("recursos",max_length=3000)
    criterio_avaliacao = models.CharField("criterio_avaliacao",max_length=3000)
    plano_aulas = models.CharField("plano_aulas",max_length=10000)

    def __str__(self):
        return self.nome
		
