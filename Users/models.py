from django.db import models


class User(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=32)
    criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Usuario(User):
    nome = models.CharField(max_length=150)
    data_nasc = models.DateField()
    igreja = models.CharField(max_length=200, null=True, blank=True)
    congregacao = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)
    cidade = models.CharField(max_length=70)
    estado = models.CharField(max_length=70)
    administrador = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
