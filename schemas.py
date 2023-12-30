from __future__ import annotations
from typing import List

from pydantic import BaseModel


class TractorBase(BaseModel):
    type: str
    year: str


class TractorCreate(TractorBase):
    pass


class Tractor(TractorBase):
    id: int
    worker_id: int

    class Config:
        orm_mode = True


class LocationBase(BaseModel):
    type: str
    address: str


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int
    worker_id: int

    class Config:
        orm_mode = True


class WorkerBase(BaseModel):
    email: str


class WorkerCreate(WorkerBase):
    password: str


class Worker(WorkerBase):
    id: int

    tractors: List[Tractor] = []
    locations: List[Location] = []

    class Config:
        orm_mode = True


class LocationUpdate(BaseModel):
    type: str
    address: str
