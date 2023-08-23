from django.db import models


class TimestampMixin(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class Product(TimestampMixin):
    id = models.UUIDField(primary_key=True, db_index=True)
    name = models.CharField(max_length=255)
    characteristic = models.ManyToManyField("Characteristic")


class Filial(TimestampMixin):
    id = models.UUIDField(primary_key=True, db_index=True)
    name = models.CharField(max_length=255)
    region = models.IntegerField()


class Characteristic(TimestampMixin):
    id = models.UUIDField(primary_key=True, db_index=True)
    self = models.ForeignKey("Characteristic", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)


class FilialPrice(TimestampMixin):
    id = models.UUIDField(primary_key=True, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    filial = models.ForeignKey(Filial, on_delete=models.DO_NOTHING)
    price = models.IntegerField()
