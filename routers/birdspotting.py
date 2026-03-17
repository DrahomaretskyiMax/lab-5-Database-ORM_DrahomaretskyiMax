from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from repositories.birdspotting import BirdspottingRepository
from models.birdspotting import Birdspotting, BirdspottingCreate

router = APIRouter(prefix="/birdspotting", tags=["Birdspotting"])


def get_birdspotting_repository(
    session: Annotated[Session, Depends(get_session)]
) -> BirdspottingRepository:
    return BirdspottingRepository(session)


@router.get("/", response_model=List[Birdspotting])
async def get_observations(
    repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]
):
    return repo.get_all()


@router.get("/{id}", response_model=Birdspotting)
async def get_observation(
    id: int,
    repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]
):
    return repo.get_one(id)


@router.post("/", response_model=Birdspotting)
async def add_birdspotting(
    payload: BirdspottingCreate,
    repo: Annotated[BirdspottingRepository, Depends(get_birdspotting_repository)]
):
    return repo.insert(payload)