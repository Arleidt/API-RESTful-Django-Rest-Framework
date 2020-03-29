from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    Implementação de um viewset que herda de viewset define um queryset e um serializer
    esse serializer criado pontoturistoserializer
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer