#import os
from fastapi import FastAPI, Depends
from fastapi import APIRouter
from helpers.config import settings, get_settings
from controllers import DataController

data_router = APIRouter(prefix="/api/data", tags=["Data"])

@data_router.get("/upload/{project_id}")
async def upload_file(project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings())):
        is_valid=DataController().validate_file(file, app_settings)
        return is_valid