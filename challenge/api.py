from typing import List
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel

from challenge.factory import delay_service_factory
from challenge.types import Flight


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"message": f"invalid request! make sure the params are valid"},
    )


class PredictionReq(BaseModel):
    flights: List[Flight]


@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {
        "status": "OK"
    }


@app.post("/predict", status_code=200)
async def post_predict(req: PredictionReq) -> dict:
    service = delay_service_factory()
    return service.predict(req.flights)
