from functools import lru_cache

from .models import AppDirectories, AppSettings


@lru_cache()
def get_app_settings() -> AppSettings:
    return AppSettings()  # pyright: ignore[reportCallIssue]


@lru_cache()
def get_app_dirs():
    return AppDirectories()
