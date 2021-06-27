from django.db import models

class Store(models.Model):
    nome = models.CharField(max_length=19, unique=True)
    owner = models.CharField(max_length=14)

    def balance(self):
        transactions_store = Transaction.objects.filter(store=self)
        return sum(transaction.transaction_io() for transaction in transactions_store)


    def __str__(self):
        return ("{}").format(self.nome)

class Transaction(models.Model):
    store = models.ForeignKey(Store, related_name='transactions', on_delete=models.CASCADE)
    date = models.DateTimeField()
    type = models.CharField(max_length=1)
    value = models.FloatField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)

    def transaction_io(self):
        if self.type in ('1', '4', '5', '6', '7', '8'):
            return self.value
        else:
            return int(self.value)*(-1)

    def transaction_date(self):
        return format(self.date, '%Y-%m-%d at %H:%M:%S')

    def __str__(self):
        type_dic = {
                    '1' : 'Débito',
                    '2'	: 'Boleto',
                    '3'	: 'Financiamento',
                    '4'	: 'Crédito',
                    '5'	: 'Recebimento Empréstimo',
                    '6'	: 'Vendas',
                    '7'	: 'Recebimento',
                    '8'	: 'Recebimento DOC',
                    '9'	: 'Aluguel',
        }

        return ("R$ {:.2f} - {} - {}").format((self.transaction_io())/100,  type_dic.__getitem__(self.type), self.transaction_date())