import json
import requests

if __name__ != '__main__':

    def obter_saldo(jobid):
        
        global closed

        response = ""
        results = ""
        
        url = f"https://api.gupy.io/api/v1/jobs/{jobid}/applications?status=hired&order=id%20asc&fields=all&perPage=10&page=1"
        headers = {"Content-Type": "application/json;charset=UTF-8",
                    "Authorization": "Bearer 6740ee9f-026d-4088-9de5-ce0ec402b004"}

        request = requests.get(url, headers=headers)
        
        try:
            response = json.loads(request.content)
            results = response['results']
        except:
            pass      

        if bool(results):

            closed = response['totalResults']      

        else:
            closed = 0
        
        if closed == None:
                closed = 0

        return closed

else:
    print("Este script não pode ser executado diretamente")