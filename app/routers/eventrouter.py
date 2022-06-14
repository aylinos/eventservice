from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from ..db.session import get_db
from ..repository import eventrepo
from ..schemas import eventschema

import requests

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter(
    prefix="/events",
    tags=['events']
)


@router.get("", response_model=List[eventschema.EventOut])
def get_all_events(db: Session = Depends(get_db)):
    return eventrepo.get_all(db)


@router.get("/{id}", response_model=eventschema.EventOut)
def get_one_event(id: int, db: Session = Depends(get_db)):
    return eventrepo.get_one(id, db)


@router.post("")
def create_event(request: eventschema.EventIn, db: Session = Depends(get_db), token = Depends(oauth2_scheme)):
    headers = {'Authorization': 'Bearer ' + token}
    r = requests.get('https://wmuomxks8g.execute-api.eu-central-1.amazonaws.com/eventor/users/id', headers=headers)
    request.creator = r.json()
    return eventrepo.create(request, db)


@router.put("/{id}", response_model=eventschema.EventOut)
def update_event(id: int, request: eventschema.EventUpdate, db: Session = Depends(get_db)):
    return eventrepo.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return eventrepo.destroy(id, db)
