from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


app = FastAPI(
    title="Sentinel",
    version="0.1"
)


class Metric(BaseModel):
    cpu: float
    ram: float
    disco: float
    sistema: str


@app.get("/")
def home():
    return {
        "sistema": "Sentinel",
        "status": "online",
        "versao": "0.1"
    }


@app.get("/status")
def status():
    return {
        "cpu": "exemplo"
    }


@app.post("/metrics")
def receber_metricas(metric: Metric):

    return {
        "recebido": True,
        "dados": metric,
        "horario": datetime.now()
    }