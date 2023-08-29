from rest_framework import viewsets
from .serializers import FilialSerializer, FilialPriceSerializer, CharacteristicSerializer, ProductSerializer
from .models import Filial, FilialPrice, Characteristic, Product
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import  HTTP_400_BAD_REQUEST


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=["get"])
    def characterictic(self, request, *args, **kwargs):
        product = self.get_object()

        serializer = CharacteristicSerializer(product.characteristic.values(), many=True)
        return Response(serializer.data)

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


