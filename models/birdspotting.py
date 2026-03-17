from typing import Optional
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

from models.birds import Bird, BirdWithSpecies


class BirdspottingBase(SQLModel):
    spotted_at: datetime
    location: str
    observer_name: str
    notes: Optional[str] = None


class Birdspotting(BirdspottingBase, table=True):
    __tablename__ = "birdspotting"

    id: Optional[int] = Field(default=None, primary_key=True)
    bird_id: int = Field(foreign_key="birds.id")

    bird: Optional[Bird] = Relationship()


class BirdspottingCreate(BirdspottingBase):
    bird_id: int


class BirdspottingWithBird(BirdspottingBase):
    id: int
    bird_id: int
    bird: BirdWithSpecies