#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import Column, Integer, String, Metadata
from sqlalchemy.ext.declerative import declerative_base

meta = Metadata()
Base = declerativ_base(metadata=meta)


class State(Base):
    __tablename__="states"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
