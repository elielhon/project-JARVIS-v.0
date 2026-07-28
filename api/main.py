from fastapi import FastAPI

from api.routes.metrics import router as metrics_router
from api.routes.status import router as status_router

app = FastAPI(
    title="Sentinel",
    version="0.1"
)


@app.get("/")
def home():
    return {
        "sistema": "Sentinel",
        "status": "online",
        "versao": "0.1"
    }


app.include_router(status_router)
app.include_router(metrics_router)