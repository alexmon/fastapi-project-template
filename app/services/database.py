'''
app.services.database
'''

import typing
import databases
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from app.config import env

DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
    env['DB_USER'],
    env['DB_PASSWORD'],
    env['DB_HOST'],
    env['DB_PORT'],
    env['DB_NAME']  
)

database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={}
)

Session = sessionmaker(bind=engine)

session = Session()
