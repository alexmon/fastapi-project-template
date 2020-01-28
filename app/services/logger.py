from typing import List
from app.config import env
import logging

logger = logging.getLogger('application-logger')
logger.setLevel(env['LOG_LEVEL'])