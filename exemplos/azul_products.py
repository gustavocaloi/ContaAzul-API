import json
import pyAzul
import time
API_URL = 'https://api.contaazul.com'

with open('./auth/token.json', 'r') as read:
    data_read = json.load(read)
    ACCESS_TOKEN = data_read['access_token']

# Exemplos de utilização
azul_produtos = pyAzul.Products(API_URL, ACCESS_TOKEN)

# Obter a lista de produtos
produtos_all = azul_produtos.get_products()
print(produtos_all)