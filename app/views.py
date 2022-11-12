from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ModelViewSet
from .serializers import BolimlarSerializers
from .serializers import Hodim_haqidaSerializers
from .serializers import HodimlarSerializers
from .serializers import QarindoshlikSerializers

from .models import Hodim_haqida,Bolimlar,Hodimlar,Qarindoshlik

class BolimlarviewSet(ModelViewSet):
    queryset = Bolimlar.objects.all()
    serializer_class = BolimlarSerializers
    http_method_names = ['get','head']

class HodimlarViewSet(ModelViewSet):
    queryset = Hodimlar.objects.all()
    serializer_class = HodimlarSerializers
    http_method_names = ['get','head']

class Hodim_haqidaViewSet(ModelViewSet):
    queryset = Hodim_haqida.objects.all()
    serializer_class = Hodim_haqidaSerializers
    http_method_names = ['get','head']

class QarindoshlikViewSet(ModelViewSet):
    queryset = Qarindoshlik.objects.all()
    serializer_class = QarindoshlikSerializers
    http_method_names = ['get','head']