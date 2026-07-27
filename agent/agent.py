import psutil
import platform
import time
import requests


API_URL = "http://127.0.0.1:8000/metrics"


def coletar_dados():

    dados = {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disco": psutil.disk_usage("C:/").percent,
        "sistema": platform.system()
    }

    return dados


while True:

    dados = coletar_dados()

    resposta = requests.post(
        API_URL,
        json=dados
    )

    print(resposta.json())

    time.sleep(5)