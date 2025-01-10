from rest_framework.viewsets import ModelViewSet
from .models import Medicament, Client
from .serializers import MedicamentoSerializer, ClienteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class MedicamentViewSet(ModelViewSet):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentoSerializer

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClienteSerializer


@api_view(['GET'])
def search_medicament(request):
    name = request.query_params.get('name', '')
    medicaments = Medicament.objects.filter(name__icontains=name)
    serializer = MedicamentoSerializer(medicaments, many=True)
    return Response(serializer.data)
