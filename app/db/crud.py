from sqlalchemy.orm import Session

from . import dbmodels, schemas

def get_history(db: Session, skip: int = 0, limit: int = 100):
    return db.query(dbmodels.History).offset(skip).limit(limit).all()

def create_history(db: Session, history: schemas.HistoryCreate):
    db_history = dbmodels.History(country=history.country, city=history.city)
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history