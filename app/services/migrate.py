import sys
from .database import engine
from .logger import logger
from app.models.user import User

def migrate():
    User.metadata.create_all(engine)

if __name__ == "__main__":
    if sys.argv[1] == "up":
        logger.debug('starting database migration')
        migrate()
        logger.debug('ending database migration')