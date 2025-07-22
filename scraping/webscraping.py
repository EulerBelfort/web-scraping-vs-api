from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import time

# Configura o ChromeDriver automaticamente
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://coinmarketcap.com/')

time.sleep(5)  # esperar a página carregar (ideal usar WebDriverWait)

rows = driver.find_elements(By.CSS_SELECTOR, 'table.cmc-table tbody tr')[:5]

data = []
for row in rows:
    name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3) p').text
    price = row.find_element(By.CSS_SELECTOR, 'td:nth-child(4) span').text
    data.append([name, price])

filename = 'data/cripto_data_selenium.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Criptomoeda', 'Preço em USD'])
    writer.writerows(data)

print(f"✅ Dados salvos em {filename}")

driver.quit()
