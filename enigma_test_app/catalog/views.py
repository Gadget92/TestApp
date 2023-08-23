from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from serializers import FilialSerializer, FilialPriceSerializer, CharacteristicSerializer, ProductSerializer
from models import Filial, FilialPrice, Characteristic, Product


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FilialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer

class FilialPriceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FilialPrice.objects.all()
    serializer_class = FilialPriceSerializer

class CharacteristicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer


