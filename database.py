from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

DATABASE_URL ="mysql+pymysql://root:mknd1234@localhost/boom"
engine = create_engine(DATABASE_URL)
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()