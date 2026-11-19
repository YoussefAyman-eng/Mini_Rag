from controllers.BaseController import BaseController
from fastapi import UploadFile


class DataController(BaseController):
    def __init__(self):
        super().__init__()


    def validate_file(self, file, app_settings):
       if file.content_type not in app_settings.file_allowed_extensions:
            return False, f"File type {file.content_type} is not allowed."

       if file.size > app_settings.file_max_size * 1024 * 1024:
            return False, f"File size exceeds the maximum limit of {app_settings.file_max_size} MB."
       
       return True, "File is valid."