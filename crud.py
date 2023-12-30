from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

import auth
import models
import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_worker(db: Session, worker_id: int):
    return db.query(models.Worker).filter(models.Worker.id == worker_id).first()


def get_worker_by_email(db: Session, email: str):
    return db.query(models.Worker).filter(models.Worker.email == email).first()


def get_workers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Worker).offset(skip).limit(limit).all()


def create_worker(db: Session, worker: schemas.WorkerCreate):
    hashed_password = auth.get_password_hash(worker.password)
    db_worker = models.Worker(email=worker.email, hashed_password=hashed_password)
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker


def get_tractors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tractor).offset(skip).limit(limit).all()


def create_worker_tractor(db: Session, tractor: schemas.TractorCreate, worker_id: int):
    db_tractor = models.Tractor(**tractor.dict(), worker_id=worker_id)
    db.add(db_tractor)
    db.commit()
    db.refresh(db_tractor)
    return db_tractor


def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()


def create_worker_location(db: Session, location: schemas.LocationCreate, worker_id: int):
    db_location = models.Location(**location.dict(), worker_id=worker_id)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location
