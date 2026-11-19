#import os
from fastapi import FastAPI, Depends, UploadFile
from fastapi import APIRouter
from helpers.config import Settings, get_settings
from controllers import DataController

data_router = APIRouter(prefix="/api/data", tags=["Data"])

#the concept of tenancy is to ensure that each tenant's data is isolated and secure, 
#preventing unauthorized access or data leakage between tenants. In a multi-tenant architecture, the application must be designed to handle multiple tenants while maintaining data privacy and security.
#file has specific class in fastapi
@data_router.get("/upload/{project_id}")
async def upload_file(project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)):
        is_valid, message = DataController().validate_file(file, app_settings)
        return is_valid, message