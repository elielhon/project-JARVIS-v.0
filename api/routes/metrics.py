from datetime import datetime

from fastapi import APIRouter

from api.schemas.metric import Metric

router = APIRouter()


@router.post("/metrics")
def receber_metricas(metric: Metric):

    return {
        "recebido": True,
        "dados": metric,
        "horario": datetime.now()
    }