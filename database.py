from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE='mysql+pymysql://root:$nivethithad25@localhost:3306/CONCERTDB'

engine=create_engine(URL_DATABASE) #creating an engine

#binding the engine with the session(local workspace for the objects of the database)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()