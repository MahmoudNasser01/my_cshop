from rest_framework import serializers

from .models import CountryCar, CompanyCar, carmodel, CarName,Products,Sections


def meta(self):
    class Meta:
        model = self
        fields = '__all__'

    return Meta
class CountrySerializer(serializers.ModelSerializer):
    Meta = meta(CountryCar)

class ManufacturerSerializer(serializers.ModelSerializer):
    Meta = meta(CompanyCar)

class CarModelSerializer(serializers.ModelSerializer):
    Meta = meta(carmodel)

class CarDetailsSerializer(serializers.ModelSerializer):
    Meta = meta(CarName)

class SectionSerializer(serializers.ModelSerializer):
    Meta = meta(Sections)
class ProductSerializer(serializers.ModelSerializer):
    Meta = meta(Products)


