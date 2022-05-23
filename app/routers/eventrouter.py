from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..db.session import get_db
from ..repository import eventrepo
from ..schemas import eventschema

router = APIRouter(
    prefix="/event",
    tags=['events']
)


@router.get("/", response_model=List[eventschema.EventOut])
def get_all_events(db: Session = Depends(get_db)):
    return eventrepo.get_all(db)


@router.get("/{id}", response_model=eventschema.EventOut)
def get_one_event(id: int, db: Session = Depends(get_db)):
    return eventrepo.get_one(id, db)


@router.post("/", response_model=eventschema.EventOut)
def create_event(request: eventschema.EventIn, db: Session = Depends(get_db)):
    return eventrepo.create(request, db)


@router.put("/{id}", response_model=eventschema.EventOut)
def update_event(id: int, request: eventschema.EventUpdate, db: Session = Depends(get_db)):
    return eventrepo.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return eventrepo.destroy(id, db)
