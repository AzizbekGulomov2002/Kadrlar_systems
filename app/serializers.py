from rest_framework import serializers
from .models import Bolimlar,Hodim_haqida,Hodimlar,Qarindoshlik


class BolimlarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bolimlar
        fields = "__all__"


class Hodim_haqidaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hodim_haqida
        fields = "__all__"

class HodimlarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hodimlar
        fields = "__all__"

class QarindoshlikSerializers(serializers.ModelSerializer):
    class Meta:
        model = Qarindoshlik
        fields = "__all__"