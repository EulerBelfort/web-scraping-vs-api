🌐 Web Scraping e API de Criptomoedas
Este projeto tem como objetivo coletar dados de criptomoedas via Web Scraping 

Estrutura do Projeto
WEB-Scraping-Cripto/
```
├── api/
│   └── api_script.py           # Script para servir os dados via API
├── data/
│   ├── cripto_data.csv         # Dados salvos da coleta
│   └── cripto_data_selenium.csv
├── scraping/
│   └── webscraping.py          # Código responsável pelo scraping
├── .gitignore                  # Arquivos/pastas ignoradas pelo Git
├── README.md                   # Instruções do projeto
└── requirements.txt            # Bibliotecas necessárias
```
Como executar o projeto
1. Clone o repositório
```
git clone https://github.com/EulerBelfort/web-scraping-vs-api.git
cd web-scraping-vs-api
```
2. Crie e ative um ambiente virtual (opcional, mas recomendado)
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
````
3. Instale as dependências
```
pip install -r requirements.txt
```
4. Execute o script de scraping
```
python scraping/webscraping.py
Isso irá coletar os dados das criptomoedas e salvar na pasta data/nome_do_arquivo.csv.
```
5. Utilizando a captura de dados usando uma  API Pública
```
python api/api_script.py
A API será iniciada e irá capturar os dados de forma dinâmica sempre precisar abrir o navegador.
```
Requisitos
Liste dos arquivos ncessários para o projeto:
Dica: Caso você encontre erros na hora de executar , use o instalador do selenium Basic
```
requests

beautifulsoup4

selenium

fastapi

pandas

uvicorn
```

Observações
O script de scraping pode usar Selenium ou requests + BeautifulSoup dependendo da fonte.

O arquivo .gitignore pode incluir o ambiente virtual e arquivos temporários.
