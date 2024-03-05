from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Pup
from .serializers import PupSerializer

class PupList(ListCreateAPIView):
    queryset = Pup.objects.all()
    serializer_class = PupSerializer

class PupDetail(RetrieveUpdateDestroyAPIView):
    queryset = Pup.objects.all()
    serializer_class = PupSerializer
