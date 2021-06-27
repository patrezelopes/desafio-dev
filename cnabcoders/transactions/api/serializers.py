from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from ..models import Transaction, Store

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class StoreBalanceSerializer(serializers.HyperlinkedModelSerializer):
    balance = SerializerMethodField()
    transactions = serializers.StringRelatedField(many=True)


    def get_balance(self, obj):
        return obj.balance()


    class Meta:
        model = Store
        fields = ['nome', 'balance', 'transactions']