from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

# We will need this for querying
#
Base.query = db_session.query_property()

class Hospitalward(Base):
    __tablename__ = 'hospitalward'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    city = Column(String)

class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    hired_on = Column(DateTime, default=func.now())
    hospitalward_id = Column(Integer, ForeignKey('hospitalward.id'))
    hospitalward = relationship(Hospitalward, backref=backref('patients', uselist=True, cascade='delete,all'))
