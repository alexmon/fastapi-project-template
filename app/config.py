# app.config

import os
from dotenv import load_dotenv
from typing import Dict
import logging

load_dotenv()

# TODO: use pudantic for declaration and validation
env: Dict[str, any] = {
    "DB_HOST": os.getenv("DB_HOST", "localhost"),
    "DB_PORT": os.getenv("DB_PORT", "5432"),
    "DB_USER": os.getenv("DB_USER", "postgres"),
    "DB_PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
    "DB_NAME": os.getenv("DB_NAME", "postgres"),
    "LOG_LEVEL": int(os.getenv("LOG_LEVEL", logging.DEBUG))
}