import requests
import csv
from datetime import datetime

import requests
import csv
from datetime import datetime
import time

#### CRIANDO UMA LISTA DAS CRIPTOS #####
cryptos = [
    'bitcoin',
    'ethereum',
    'ripple',
    'cardano',
    'solana'
]

#### ACESSANDO API ####
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    'ids': ','.join(cryptos),
    'vs_currencies': 'usd',
    'include_last_updated_at': 'true'
}

# RESPOSTA DO SERVIDOR
response = requests.get(url,params=params)

# RETORNO DO STATUS DO SERVIDOR
if response.status_code == 200:
    # RETORNO EM FORMATO JSON
    data = response.json()
    
    # CAMINHO DO ARQUIVO CSV
    filename = 'data/cripto_data.csv'

    # ESCREVENDO DADOS NO ARQUIVO CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Criptomoeda', 'Preço em USD', 'Última atualização (UTC)'])

        for coin in cryptos:
            price = data[coin]['usd']
            updated_at = datetime.utcfromtimestamp(data[coin]['last_updated_at']).strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([coin, price, updated_at])

    print(f"✅ Dados salvos com sucesso em '{filename}'")

else:
    print(f"❌ Erro ao acessar a API: {response.status_code}")
