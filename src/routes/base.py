#import os
from fastapi import FastAPI, Depends
from fastapi import APIRouter
from helpers.config import settings, get_settings

base_router = APIRouter(prefix="/api/base", tags=["Base"])

@base_router.get("/")
async def welcome_message(app_settings: Settings = Depends(get_settings())):
        app_name = app_settings.get("app_name")
        app_version = app_settings.get("app_version")
        #app_version=os.getenv('APP_VERSION')
        #app_name=os.getenv('APP_NAME')
        return {"app_name": app_name, "app_version": app_version}
    