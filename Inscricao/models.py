from django.db import models
from Users.models import Usuario
from Eventos.models import Eventos


class Inscricao(models.Model):
    status = models.BooleanField()
    usuario = models.ForeignKey(Usuario, related_name='usuario', on_delete=models.CASCADE)
    evento = models.ForeignKey(Eventos, related_name='evento', on_delete=models.CASCADE)
    pago = models.BooleanField()
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario
