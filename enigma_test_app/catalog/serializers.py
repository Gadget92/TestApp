from .models import Filial, Product, FilialPrice, Characteristic
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "characteristic"]

    def create(self, validated_data):
        product, created = Product.objects.update_or_create(
            id=validated_data.get('id', None),
            defaults={
                'name': validated_data.get('name', None),
                'characteristic': validated_data.get('characteristic', None)
            })
        return product

    def update(self, instance, validated_data):
        return self.create(validated_data)


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = ["id", "name", "region"]

    def create(self, validated_data):
        filial, created = Filial.objects.update_or_create(
            id=validated_data.get('id', None),
            defaults={
                'name': validated_data.get('name', None),
                'region': validated_data.get('region', None)
            })
        return filial

    def update(self, instance, validated_data):
        return self.create(validated_data)


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ["id", "self", "name"]

    def create(self, validated_data):
        characteristic, created = Characteristic.objects.update_or_create(
            id=validated_data.get('id', None),
            defaults={
                'self': validated_data.get('self', None),
                'name': validated_data.get('name', None)
            })
        return characteristic

    def update(self, instance, validated_data):
        return self.create(validated_data)


class FilialPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilialPrice
        fields = ["id", "product", "filial", "price"]

    def create(self, validated_data):
        filial_price, created = FilialPrice.objects.update_or_create(
            id=validated_data.get('id', None),
            defaults={
                'product': validated_data.get('product', None),
                'filial': validated_data.get('filial', None),
                'price': validated_data.get('price', None)
            })
        return filial_price

    def update(self, instance, validated_data):
        return self.create(validated_data)
