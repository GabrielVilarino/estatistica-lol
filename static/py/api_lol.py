import requests

class Api:
    URL_BASE_AMERICAS = 'https://americas.api.riotgames.com'
    URL_BASE_BR1 = 'https://br1.api.riotgames.com'

    def __init__(self):
        self.api_key = 'RGAPI-63df61b3-be06-4e0f-bf27-c472c776d0be'
        self.headers = {
            'X-Riot-Token': self.api_key
        }


    def obter_puuid_jogador(self,
                            game_name : str,
                            tag_line : str) -> str:
        """
        Parâmetros

        - game_name: Nome do Invocador
        - tag_line: Tag do Jogador

        Função faz uma requisição get para a api esperando o retorno
        do puuid do jogador.
        """
        url_puuid = Api.URL_BASE_AMERICAS + f'/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}'

        response = requests.get(url_puuid, headers=self.headers)

        if response.status_code == 200:
            # Dados do invocador
            data = response.json()
            return data
        else:
            return None
        

    def obter_icone_jogador(self,
                            puuid : str):
        """
        Parâmetros

        - puuid: puuid do jogador

        Função faz uma requisição get para a api esperando o retorno
        do id do icone do jogador.
        """

        url_icone = Api.URL_BASE_BR1 + f'/lol/summoner/v4/summoners/by-puuid/{puuid}'

        response = requests.get(url_icone, headers=self.headers)

        if response.status_code == 200:
            # Dados do invocador
            data = response.json()
            id_icone = data['profileIconId']
            return id_icone
        else:
            return None