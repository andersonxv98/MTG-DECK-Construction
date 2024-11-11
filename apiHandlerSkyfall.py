import requests

class Api:
    def __init__(self):
        self.url = "https://api.scryfall.com/"

    def getCardByName(self, name):
        endpointWithParam = "cards/named?exact="
        response = requests.get(self.url+endpointWithParam+name)
        if response.status_code == 200:
            # Obtém o conteúdo da resposta como texto
            conteudo = response.text
            #print('Conteúdo da resposta:', conteudo)
            
            # Ou, se a resposta for JSON, você pode decodificá-la assim
            dados_json = response.json()
            #print('Dados JSON:', dados_json)
            return dados_json
        elif response.status_code == 404:
            print(f'Falha na requisição: {response.status_code}')
            return "Erro"
        else:
            print(f'Falha na requisição: {response.status_code}')
            return "Erro"