from rest_framework.serializers import ModelSerializer
from Inscricao.models import Inscricao


class InscricaoSerializer(ModelSerializer):
    class Meta:
        model = Inscricao
        fields = ('id', 'status', 'usuario', 'evento', 'pago', 'criacao')
