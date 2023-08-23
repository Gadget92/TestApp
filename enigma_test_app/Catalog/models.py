from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    characteristic = models.ManyToManyField("Characteristic")


class Filial(models.Model):
    name = models.CharField(max_length=255)
    region = models.IntegerField()


class Characteristic(models.Model):
    self = models.ForeignKey("Characteristic", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)


class FilialPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    filial = models.ForeignKey(Filial, on_delete=models.DO_NOTHING)
    price = models.IntegerField()
