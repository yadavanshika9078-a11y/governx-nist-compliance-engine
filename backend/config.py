import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """
    Application configuration.
    All project settings are managed from here.
    """

    SECRET_KEY = os.getenv("SECRET_KEY", "governx-secret-key")

    DEBUG = os.getenv("DEBUG", "True") == "True"

    APP_NAME = "GovernX"

    VERSION = "1.0.0"

    DATA_FOLDER = "backend/data"

    LOG_FOLDER = "backend/logs"