from fastapi import APIRouter, FastAPI

from .views import data_aggregation, data_outliers


def init_routes():
    router = APIRouter(prefix="/statistics")

    router.add_api_route("/aggregation", data_aggregation, methods={"POST"})
    router.add_api_route("/outliers", data_outliers, methods={"POST"})

    return router


def init_app(app: FastAPI):
    app.include_router(init_routes())
