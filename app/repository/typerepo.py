from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models import type
from app.schemas import typeschema


def get_all(db: Session):
    types = db.query(type.Type).all()
    return types


def get_one(id: int, db: Session):
    found_type = db.query(type.Type).filter(type.Type.id == id).first()
    if not found_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Type with id: {id} is not available")
    return found_type


def create(request: typeschema.TypeIn, db: Session):
    # Catch title already exists exception
    new_type = type.Type(title=request.title)
    db.add(new_type)
    db.commit()
    db.refresh(new_type)
    return new_type


def update(id: int, request: typeschema.TypeUpdate, db: Session):
    # Check if user from cookie is admin
    # Catch title already exists exception
    found_type = db.query(type.Type).filter(type.Type.id == id)

    if not found_type.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Type with id {id} not found")

    if request.title:
        found_type.update(request.dict(exclude_unset=True))
        db.commit()
    return found_type.first()


def destroy(id: int, db: Session):
    # Check if user from cookie is admin
    found_type = db.query(type.Type).filter(type.Type.id == id)

    if not found_type.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Type with id {id} not found")

    found_type.delete(synchronize_session=False)
    db.commit()
    return True
