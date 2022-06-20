import fastapi

from fastapi import Depends

from sqlalchemy.orm import Session

from typing import List

from models.location import Location

from db import crud, dbmodels, schemas
from db.database import SessionLocal, engine


dbmodels.Base.metadata.create_all(bind = engine)


def get_db():
    """Get DB from session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = fastapi.APIRouter()


@router.post("/history/add", response_model = schemas.History)
def create_history(history: schemas.HistoryCreate, db: Session = Depends(get_db), location: Location = fastapi.Depends()):
    """Add history to DB"""
    history.country = location.country
    history.city = location.city
    return crud.create_history(db = db, history = history)


@router.get("/history", response_model = List[schemas.History])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Read from DB"""
    history = crud.get_history(db, skip = skip, limit = limit)
    return history
