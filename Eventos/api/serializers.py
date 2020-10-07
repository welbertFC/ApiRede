from rest_framework.serializers import ModelSerializer
from Eventos.models import Eventos


class EventoSerializer(ModelSerializer):
    class Meta:
        model = Eventos
        fields = ('id', 'data', 'horario_inicio', 'horario_termino',
                  'titulo', 'descricao', 'vagas', 'valor')
