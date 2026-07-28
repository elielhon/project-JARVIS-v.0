import psutil
import platform
import time
import requests

from config.config import METRICS_ENDPOINT, AGENT_INTERVAL


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

try:
    resposta = requests.post(
        METRICS_ENDPOINT,
        json=dados,
        timeout=5
    )

    print("✔ Dados enviados com sucesso!")
    print(resposta.json())

except requests.exceptions.RequestException as erro:
    print(f"✘ Erro ao enviar dados: {erro}")

    time.sleep(AGENT_INTERVAL)