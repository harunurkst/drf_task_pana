from rest_framework import serializers
from .models import Divisions, Districts, Thana


class DivisionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    photo = serializers.ImageField()

    def create(self, validated_data):
        return Divisions.objects.create(**validated_data)


class DistrictSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    division = DivisionSerializer()

    def create(self, validated_data):
        dist_name = validated_data.get('name')
        div_name = validated_data['division']['name']
        div_obj = Divisions.objects.get(name=div_name)
        Districts.objects.create(name=dist_name, division=div_obj)
        return validated_data


class ThanaSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    districts = DistrictSerializer()

    def create(self, validated_data):
        thana_name = validated_data['name']
        dist_name = validated_data['districts']['name']
        dist_obj = Districts.objects.get(name=dist_name)
        Thana.objects.create(name=thana_name, districts=dist_obj)
        return validated_data
