# importar o App, Builder (GUI)
# # criar o nosso aplicativo
# # criar a função build

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI

#Usando a API que a economia.awesomeapi.com.br disponibiliza para cotações de moeda. 
#Atualizada a cada 30 segundos
# https://economia.awesomeapi.com.br/last/USD-BRL
# https://economia.awesomeapi.com.br/last/EUR-BRL
# https://economia.awesomeapi.com.br/last/BTC-BRL
# https://economia.awesomeapi.com.br/last/RTH-BRL

##  Formatação da resposta do JSON para USD-BRL
##  "USDBRL":{
##     "code":"USD",
##     "codein":"BRL",
##     "name":"Dólar Americano/Real Brasileiro",
##     "high":"5.698",
##    "low":"5.637",
##     "varBid":"0.0267",
##     "pctChange":"0.47",
##     "bid":"5.6792",
##     "ask":"5.6805",
##     "timestamp":"1638798264",
##     "create_date":"2021-12-06 10:44:24"
##  }

    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R$ {self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R$ {self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R$ {self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R$ {self.pegar_cotacao('ETH')}"


    def pegar_cotacao(self, currency):
        x_url          = f"https://economia.awesomeapi.com.br/last/{currency}-BRL"
        x_request      = requests.get(x_url)
        x_request_json = x_request.json()
        currency = x_request_json[f"{currency}BRL"]["bid"]
        return currency


MeuAplicativo().run()
