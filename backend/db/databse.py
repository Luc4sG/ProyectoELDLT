from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv.main import load_dotenv
import os

load_dotenv()

try: 
    engine = create_engine(os.getenv('DATABASE_URL'))
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except Exception as e:
    print("Error creando engine: ", e)


# TODO: ver que onda el context manager
