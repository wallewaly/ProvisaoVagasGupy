import requests
import json
from . import prepara_carga

results = '0'
page = 1

if __name__ != '__main__':

    def obter_dados_vaga() -> object:

        global results, page

        print("Obtendo dados das vagas na base da Gupy")

        while results:

            url = f"https://api.gupy.io/api/v1/jobs?fields=all&perPage=200&page={page}"
            header = {"Content-Type": "application/json;charset=UTF-8",
                    "Authorization": "Bearer <API Key>"}

            request = requests.get(url, headers=header)
            response = json.loads(request.content)

            results = response['results']

            if bool(results):

                prepara_carga.gerar(results,page)

            page = page + 1

else:
    print("Este script não pode ser executado diretamente")
