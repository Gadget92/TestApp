from django.urls import include, path
from rest_framework import routers
from catalog import views

router = routers.DefaultRouter()
router.register(r'filial', views.FilialViewSet)
router.register(r'product', views.ProductViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]