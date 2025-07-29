from tkinter import *
import requests

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Bitcoin: {cotacao_btc}
    '''

    print(texto)

janela = Tk()

####  CONTEÚDO DA APLICAÇÃO ###

# TITULO DA APLICAÇÃO
janela.title("Cotação de Moedas")

# TEXTO 1
texto_orientacao = Label(janela, text="Clique no botão para buscar a cotação")
# GRID
texto_orientacao.grid(column=0, row=0)
# BOTÃO
botao = Button(janela, text="BUSCAR COTAÇÕES", command=pegar_cotacoes)
botao.grid(column=0,row=1)
#  CHAMANDO A JANELA DA APLICAÇÃO
janela.mainloop()