from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "products"

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("", views.main),
]