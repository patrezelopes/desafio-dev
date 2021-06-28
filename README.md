# get repository
git clone https://github.com/patrezelopes/desafio-dev.git

# create containers web e db
cd ./desafio-dev/cnabcoders

docker-compose up --build -d

# Access and upload transactions
if you access from ip, replace 127.0.0.1 to <your_ip> in all this document

[click login](http://127.0.0.1:8000)

usuario teste, password teste

# Register a new application
Access [link register](http://127.0.0.1:8000/authenticate/applications/register/) and register application with this values:

|  Application fields|  |
| --- | --- 
| name |bycoders_auth
|client_id|FMWr3BkTUuYQRdP2gAVmj1a7DdnvOGg25apiHgkb
|client_secret|APwMBjwNmQaSDza6iHzNhZvraSmWl4GYpAUdrbR0gKB2aQ675Qnd6t7zSGvrEXErfkpjThEPcyjzhl8vP5CZJ0L48T36AZVkfsrrTbYB0w9WDdpKDUKwVmzNzAoUzoKl
|client_type | confidential
|authorization_grant_type | authorization_grant_type
|redirect_uris | http://127.0.0.1:8000/
|algorithm | No OIDC support

You are redirect to [upload link](http://127.0.0.1:8000/transactions/upload)
choose file
Upload file CNAB.txt

# List transactions
Access [list link](http://127.0.0.1:8000/transactions/list) in left bar

In this part, it will showing the Stores and your self Balance. 
Click on plus button ("+") to showing Store transactions


endpoint:

 [transactions list](http://127.0.0.1:8000/transactions/api/list/)
 ```
 [
    {
        "url": "http://127.0.0.1:8000/transactions/api/list/1/",
        "date": "2019-03-01T15:34:53Z",
        "type": "3",
        "value": 1420.0,
        "cpf": "09620676017",
        "card": "4753****3153",
        "store": "http://127.0.0.1:8000/transactions/api/balance/1/"
    },
    {
        "url": "http://127.0.0.1:8000/transactions/api/list/2/",
        "date": "2019-03-01T14:56:07Z",
        "type": "5",
        "value": 1320.0,
        "cpf": "55641815063",
        "card": "3123****7687",
        "store": "http://127.0.0.1:8000/transactions/api/balance/2/"
    },
 ...
]
```

[Balance Store's](http://127.0.0.1:8000/transactions/api/balance/)
```
[
    {
        "nome": "BAR DO JOÃO       ",
        "balance": -1020.0,
        "transactions": [
            "R$ -14.20 - Financiamento - 2019-03-01 at 15:34:53",
            "R$ -11.20 - Boleto - 2019-03-01 at 23:42:34",
            "R$ 15.20 - Débito - 2019-03-01 at 23:30:00"
        ]
    },
    {
        "nome": "LOJA DO Ó - MATRIZ",
        "balance": 2300.0,
        "transactions": [
            "R$ 13.20 - Recebimento Empréstimo - 2019-03-01 at 14:56:07",
            "R$ 20.00 - Débito - 2019-03-01 at 09:00:02",
            "R$ -10.20 - Aluguel - 2019-03-01 at 00:00:00"
        ]
    },
...
]
```
curl testing

curl -X POST http://127.0.0.1:8000/authenticate/token/ -H "content-type: application/x-www-form-urlencoded" -d "grant_type=password&client_id=FMWr3BkTUuYQRdP2gAVmj1a7DdnvOGg25apiHgkb&client_secret=APwMBjwNmQaSDza6iHzNhZvraSmWl4GYpAUdrbR0gKB2aQ675Qnd6t7zSGvrEXErfkpjThEPcyjzhl8vP5CZJ0L48T36AZVkfsrrTbYB0w9WDdpKDUKwVmzNzAoUzoKl&username=teste&password=teste
curl --request GET \
  --url http://127.0.0.1:8000/transactions/list \
  --header 'Authorization: Bearer <token>' \
  --cookie csrftoken=<token>
  
curl --request GET \
  --url http://127.0.0.1:8000/transactions/api/balance/ \
  --header 'Authorization: Bearer JHwHHiRCxLp1FZfyrvDr0aOC1FhufL' \
  --cookie csrftoken=67MlRCgIp9RE6HRwDlFjw3yhzJfcMlgP0DI7RUZCvcpkgmGRMj4AmTXxMDt7LwSf

**for more**
# Run django shell
run web python manage.py shell

# Down containers web e db
docker-compose down


# Desafio programação - para vaga desenvolvedor

Por favor leiam este documento do começo ao fim, com muita atenção.
O intuito deste teste é avaliar seus conhecimentos técnicos em programação.
O teste consiste em parsear [este arquivo de texto(CNAB)](https://github.com/ByCodersTec/desafio-ruby-on-rails/blob/master/CNAB.txt) e salvar suas informações(transações financeiras) em uma base de dados a critério do candidato.
Este desafio deve ser feito por você em sua casa. Gaste o tempo que você quiser, porém normalmente você não deve precisar de mais do que algumas horas.

# Instruções de entrega do desafio

1. Primeiro, faça um fork deste projeto para sua conta no Github (crie uma se você não possuir).
2. Em seguida, implemente o projeto tal qual descrito abaixo, em seu clone local.
3. Por fim, envie via email o projeto ou o fork/link do projeto para seu contato Bycoders_ com cópia para rh@bycoders.com.br.

# Descrição do projeto

Você recebeu um arquivo CNAB com os dados das movimentações finanaceira de várias lojas.
Precisamos criar uma maneira para que estes dados sejam importados para um banco de dados.

Sua tarefa é criar uma interface web que aceite upload do [arquivo CNAB](https://github.com/ByCodersTec/desafio-ruby-on-rails/blob/master/CNAB.txt), normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

**Sua aplicação web DEVE:**

1. Ter uma tela (via um formulário) para fazer o upload do arquivo(pontos extras se não usar um popular CSS Framework )
2. Interpretar ("parsear") o arquivo recebido, normalizar os dados, e salvar corretamente a informação em um banco de dados relacional, **se atente as documentações** que estão logo abaixo.
3. Exibir uma lista das operações importadas por lojas, e nesta lista deve conter um totalizador do saldo em conta
4. Ser escrita na sua linguagem de programação de preferência
5. Ser simples de configurar e rodar, funcionando em ambiente compatível com Unix (Linux ou Mac OS X). Ela deve utilizar apenas linguagens e bibliotecas livres ou gratuitas.
6. Git com commits atomicos e bem descritos
7. PostgreSQL, MySQL ou SQL Server
8. Ter testes automatizados
9. Docker compose (Pontos extras se utilizar)
10. Readme file descrevendo bem o projeto e seu setup
11. Incluir informação descrevendo como consumir o endpoint da API

**Sua aplicação web não precisa:**

1. Lidar com autenticação ou autorização (pontos extras se ela fizer, mais pontos extras se a autenticação for feita via OAuth).
2. Ser escrita usando algum framework específico (mas não há nada errado em usá-los também, use o que achar melhor).
3. Documentação da api.(Será um diferencial e pontos extras se fizer)

# Documentação do CNAB

| Descrição do campo  | Inicio | Fim | Tamanho | Comentário
| ------------- | ------------- | -----| ---- | ------
| Tipo  | 1  | 1 | 1 | Tipo da transação
| Data  | 2  | 9 | 8 | Data da ocorrência
| Valor | 10 | 19 | 10 | Valor da movimentação. *Obs.* O valor encontrado no arquivo precisa ser divido por cem(valor / 100.00) para normalizá-lo.
| CPF | 20 | 30 | 11 | CPF do beneficiário
| Cartão | 31 | 42 | 12 | Cartão utilizado na transação 
| Hora  | 43 | 48 | 6 | Hora da ocorrência atendendo ao fuso de UTC-3
| Dono da loja | 49 | 62 | 14 | Nome do representante da loja
| Nome loja | 63 | 81 | 19 | Nome da loja

# Documentação sobre os tipos das transações

| Tipo | Descrição | Natureza | Sinal |
| ---- | -------- | --------- | ----- |
| 1 | Débito | Entrada | + |
| 2 | Boleto | Saída | - |
| 3 | Financiamento | Saída | - |
| 4 | Crédito | Entrada | + |
| 5 | Recebimento Empréstimo | Entrada | + |
| 6 | Vendas | Entrada | + |
| 7 | Recebimento TED | Entrada | + |
| 8 | Recebimento DOC | Entrada | + |
| 9 | Aluguel | Saída | - |

# Avaliação

Seu projeto será avaliado de acordo com os seguintes critérios.

1. Sua aplicação preenche os requerimentos básicos?
2. Você documentou a maneira de configurar o ambiente e rodar sua aplicação?
3. Você seguiu as instruções de envio do desafio?
4. Qualidade e cobertura dos testes unitários.

Adicionalmente, tentaremos verificar a sua familiarização com as bibliotecas padrões (standard libs), bem como sua experiência com programação orientada a objetos a partir da estrutura de seu projeto.

# Referência

Este desafio foi baseado neste outro desafio: https://github.com/lschallenges/data-engineering

---

Boa sorte!
