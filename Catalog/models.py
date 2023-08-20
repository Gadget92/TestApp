from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)


class Filial(models.Model):
    name = models.CharField(max_length=255)
    region = models.IntegerField()


class Characteristic(models.Model):
    self = models.ForeignKey("Characteristic", on_delete=None)
    name = models.CharField(max_length=255)
    product = models.ManyToManyField(Product)


class FilialPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=None)
    filial = models.ForeignKey(Filial, on_delete=None)
    price = models.IntegerField()
