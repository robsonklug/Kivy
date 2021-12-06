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

    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R$ {self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R$ {self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R$ {self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R$ {self.pegar_cotacao('ETH')}"
        

    def pegar_cotacao(self, currency):
        link           = f"https://economia.awesomeapi.com.br/last/{currency}-BRL"
        x_request      = requests.get(link)
        x_request_json = x_request.json()
        currency = x_request_json[f"{currency}BRL"]["bid"]
        return currency


MeuAplicativo().run()
