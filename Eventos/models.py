from django.db import models


class Eventos(models.Model):
    data = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    horario_inicio = models.TimeField()
    horario_termino = models.TimeField()
    titulo = models.CharField(max_length=500)
    descricao = models.TextField()
    vagas = models.IntegerField()
    valor = models.CharField(max_length=100)
    url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo
