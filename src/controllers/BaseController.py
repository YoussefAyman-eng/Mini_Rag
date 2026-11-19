from helpers.config import get_settings
#all controllers can see settings easily by inheriting from BaseController

class BaseController:
    def __init__(self):
        self.app_settings = get_settings()

    