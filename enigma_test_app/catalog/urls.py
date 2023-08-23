from django.urls import include, path
from rest_framework import routers
from .views import FilialViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'filial', FilialViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('catalog/', include(router.urls)),
]