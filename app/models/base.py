# app.models.base

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, func

class Base(object):
    created_at =  Column(DateTime, default=func.now())
    updated_at =  Column(DateTime, default=func.now())
    deleted_at =  Column(DateTime, default=None)

Base = declarative_base(cls=Base)