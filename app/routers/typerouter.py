from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repository import typerepo
from app.schemas import typeschema

router = APIRouter(
    prefix="/type",
    tags=['types']
)


@router.get("/", response_model=List[typeschema.TypeOut])
def get_all_types(db: Session = Depends(get_db)):
    return typerepo.get_all(db)


@router.get("/{id}", response_model=typeschema.TypeOut)
def get_one_type(id: int, db: Session = Depends(get_db)):
    return typerepo.get_one(id, db)


@router.post("/", response_model=typeschema.TypeOut)
def create_type(request: typeschema.TypeIn, db: Session = Depends(get_db)):
    return typerepo.create(request, db)


@router.put("/{id}", response_model=typeschema.TypeOut)
def update_type(id: int, request: typeschema.TypeUpdate, db: Session = Depends(get_db)):
    return typerepo.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return typerepo.destroy(id, db)
