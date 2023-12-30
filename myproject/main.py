from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import os

import auth
import crud
import models
import schemas
from database import SessionLocal, engine


print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    worker = auth.authenticate_worker(db, form_data.username, form_data.password)
    if not worker:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": worker.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/workers/", response_model=schemas.Worker)
def create_worker(
        worker: schemas.WorkerCreate, db: Session = Depends(get_db)
):
    db_workermail = crud.get_worker_by_email(db, email=worker.email)
    if db_workermail:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_worker(db=db, worker=worker)


@app.get("/workers/", response_model=list[schemas.Worker])
def read_workers(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme)
):
    workers = crud.get_workers(db, skip=skip, limit=limit)
    return workers


@app.get("/workers/{worker_id}", response_model=schemas.Worker)
def read_worker(worker_id: int, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    db_worker = crud.get_worker(db, worker_id=worker_id)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="worker not found")
    return db_worker


@app.post("/workers/{worker_id}/tractors/", response_model=schemas.Tractor)
def create_tractor_for_worker(
        worker_id: int, tractor: schemas.TractorCreate, db: Session = Depends(get_db)
):
    return crud.create_worker_tractor(db=db, tractor=tractor, worker_id=worker_id)


@app.get("/tractors/", response_model=list[schemas.Tractor])
def read_tractors(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme)
):
    tractors = crud.get_tractors(db, skip=skip, limit=limit)
    return tractors


@app.get("/locations/", response_model=list[schemas.Location])
def read_locations(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme)
):
    locations = crud.get_locations(db, skip=skip, limit=limit)
    return locations


@app.post("/workers/{worker_id}/locations/", response_model=schemas.Location)
def create_location_for_worker(
        worker_id: int, location: schemas.LocationCreate, db: Session = Depends(get_db)
):
    return crud.create_worker_location(db=db, location=location, worker_id=worker_id)


@app.delete("/tractors/{tractor_id}", response_model=schemas.Tractor)
def delete_tractor(tractor_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    # Check if the Tractor exists
    db_tractor = db.query(models.Tractor).filter(models.Tractor.id == tractor_id).first()
    if db_tractor is None:
        raise HTTPException(status_code=404, detail="Tractor not found")

    # Delete the Tractor
    db.delete(db_tractor)
    db.commit()

    return db_tractor


@app.put("/workers/{worker_id}/locations/{location_id}", response_model=schemas.Location)
def update_worker_location(
    worker_id: int,
    location_id: int,
    location: schemas.LocationUpdate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    # Check if the worker exists
    db_worker = crud.get_worker(db, worker_id=worker_id)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")

    # Check if the location exists
    db_location = db.query(models.Location).filter(models.Location.id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")

    # Update the location
    for key, value in location.dict().items():
        setattr(db_location, key, value)

    db.commit()
    db.refresh(db_location)
    return db_location
