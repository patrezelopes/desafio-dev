from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, authentication, exceptions, status


from .serializers import TransactionSerializer, StoreBalanceSerializer
from ..models import Transaction, Store


class TransactionViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class StoreBalanceViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    queryset = Store.objects.all()
    serializer_class = StoreBalanceSerializer

    def get_queryset(self):
        nome = self.request.GET.get('search[value]')
        if nome:
            self.queryset = self.queryset.filter(nome__icontains=nome)
        return self.queryset
