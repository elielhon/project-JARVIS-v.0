from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from database.database import Base


class Metric(Base):

    __tablename__ = "metrics"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    cpu = Column(
        Float
    )

    ram = Column(
        Float
    )

    disco = Column(
        Float
    )

    sistema = Column(
        String
    )

    data_hora = Column(
        DateTime,
        default=datetime.now
    )