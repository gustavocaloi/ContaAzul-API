import json
import pyAzul
import time
API_URL = 'https://api.contaazul.com'

with open('./auth/token.json', 'r') as read:
    data_read = json.load(read)
    ACCESS_TOKEN = data_read['access_token']

# Exemplos de utilização
#azul_produtos = pyAzul.Products(API_URL, ACCESS_TOKEN)
#azul_services = pyAzul.Services(API_URL, ACCESS_TOKEN)
azul_sales = pyAzul.Sales(API_URL, ACCESS_TOKEN)

# Todas as vendas.
vendas_all = azul_sales.get_sales()
print(vendas_all)


# Vendas por filtro.
#vendas_dia = azul_sales.get_sales(emission_start='01/07/2022', emission_end='01/08/2022')
#print(vendas_dia)

#azul_sales.get_sales(status='COMMITTED')
#azul_sales.get_sales(size=1)

# Vendas por Id.
#azul_sales.get_sales_byId('70f31792-e898-418d-9eea-fae274b4763f')
#azul_sales.new_sale(nova_venda_body)  # Enviar nova venda.

