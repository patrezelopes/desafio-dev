from . import views
from django.urls import path, include
from rest_framework import routers
from .api.viewsets import TransactionViewSet, StoreBalanceViewSet

router = routers.DefaultRouter()
router.register(r'list', TransactionViewSet)
router.register(r'balance', StoreBalanceViewSet)



urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('list/', views.list, name='list'),
    path('api/', include(router.urls)),
    ]