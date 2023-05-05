from sqlalchemy.orm import Session
import sys

sys.path.append("..")
from db import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()