import platform

import psutil
from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
def status():

    return {
        "cpu": f"{psutil.cpu_percent()}%",
        "ram": f"{psutil.virtual_memory().percent}%",
        "disco": f"{psutil.disk_usage('C:/').percent}%",
        "sistema": platform.system()
    }