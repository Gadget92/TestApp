from django.db import models

class Filial(models.Model):
    name = models.CharField(max_length=255)
    region = models.IntegerField()
    filial_price = models.ForeignKey("Filial", on_delete=None)

class Product(models.Model):
    name = models.CharField(max_length=255)
    characteristic = models.ManyToManyField("Characteristic")

class FilialPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=None)
    price = models.IntegerField()

class Characteristic(models.Model):
    self = models.ForeignKey("Characteristic", on_delete=None)
    name = models.CharField(max_length=255)
