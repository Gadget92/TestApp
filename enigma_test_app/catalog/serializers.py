from models import Filial, Product, FilialPrice, Characteristic
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "characteristic"]


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = ["name", "region"]


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ["self", "name"]


class FilialPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilialPrice
        fields = ["product", "filial", "price"]
