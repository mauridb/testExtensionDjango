from rest_framework import serializers
from data_wizard import registry
from .models import FileModel


class FileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = '__all__'

registry.register("Time Series", FileModelSerializer)