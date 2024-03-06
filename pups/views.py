from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Pup
from .serializers import PupSerializer
from .permissions import IsOwnerOrReadOnly

class PupList(ListCreateAPIView):
    queryset = Pup.objects.all()
    serializer_class = PupSerializer

class PupDetail(RetrieveUpdateDestroyAPIView):
    queryset = Pup.objects.all()
    serializer_class = PupSerializer
    permission_classes = (IsOwnerOrReadOnly,)
