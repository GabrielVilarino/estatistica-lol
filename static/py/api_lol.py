import requests

class Api:
    URL_BASE_AMERICAS = 'https://americas.api.riotgames.com'
    URL_BASE_BR1 = 'https://br1.api.riotgames.com'

    def __init__(self):
        self.api_key = 'RGAPI-96882626-bfb4-4852-9148-e3f906744140'
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
            puuid = data['puuid']
            return puuid
        else:
            return None