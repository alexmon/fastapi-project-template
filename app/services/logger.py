'''
app.services.logger
'''

from typing import List
import logging
from app.config import env

logger = logging.getLogger('application-logger')
logger.setLevel(env['LOG_LEVEL'])
