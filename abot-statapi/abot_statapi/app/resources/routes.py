from fastapi import FastAPI


def init_app(app: FastAPI):
    """Initialize routes, middleware, sub-apps, etc. to the given Application"""
    from . import statistics

    statistics.init_app(app)
