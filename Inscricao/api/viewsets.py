from rest_framework.viewsets import ModelViewSet
from .serializers import InscricaoSerializer
from Inscricao.models import Inscricao


class InscricaoViewSet(ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer
