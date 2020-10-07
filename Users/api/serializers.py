from rest_framework.serializers import ModelSerializer
from Users.models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'email', 'senha', 'nome', 'data_nasc',
                  'igreja', 'congregacao', 'endereco', 'cidade',
                  'estado', 'administrador')
