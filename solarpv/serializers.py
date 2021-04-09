from rest_framework import serializers
from .models import Product, Certificate, Service, Location, Client, PerformanceData, TestSequence, TestStandard


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class PerformanceDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerformanceData
        fields = "__all__"

class TestSequenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestSequence
        fields = "__all__"

class TestStandardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestStandard
        fields = "__all__"

