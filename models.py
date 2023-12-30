from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    tractors = relationship("Tractor", back_populates="owner")
    locations = relationship("Location", back_populates="owner")


class Tractor(Base):
    __tablename__ = "tractor"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    year = Column(String, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))

    owner = relationship("Worker", back_populates="tractors")


class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    address = Column(String, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))

    owner = relationship("Worker", back_populates="locations")
