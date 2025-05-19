from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
url_postgre = "postgresql://postgres:postgres@host.docker.internal:5437/etl_ml"
engine = create_engine(url_postgre, echo=True)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)
