from pydantic import BaseModel


class Metric(BaseModel):
    cpu: float
    ram: float
    disco: float
    sistema: str