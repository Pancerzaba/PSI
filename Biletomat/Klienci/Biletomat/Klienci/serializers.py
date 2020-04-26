from rest_framework import serializers
from models import Klient

class SnippetSerializer(serializers.Serializer):
    id = serializers.AutoField(read_only=True)
    imie = serializers.CharField(required=True, allow_blank=True, max_length=50)
    nazwisko = serializers.CharField(required=True, allow_blank=True, max_length=50)
    e_mail = serializers.CharField(required=True, max_length=150)
    miasto = serializers.CharField(required=True, allow_blank=True, max_length=50)
    ulica = serializers.CharField(required=True, allow_blank=True, max_length=50)

    def create(self, validated_data):
        return Klient.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.imie = validate_data.get('Imie', instance.imie)
        instance.nazwisko = validate_data.get('Nazwisko', instance.nazwisko)
        instance.e_mail = validate_data.get('E-Mail', instance.e_mail)
        instance.miasto = validate_data.get('Miasto', instance.miasto)
        instance.save()
        return instance