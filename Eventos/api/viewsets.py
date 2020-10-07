from rest_framework.viewsets import ModelViewSet
from Eventos.models import Eventos
from .serializers import EventoSerializer


class EventoViewSet(ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventoSerializer
