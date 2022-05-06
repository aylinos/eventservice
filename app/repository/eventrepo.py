from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import event
from app.schemas import eventschema


def get_all(db: Session):
    # User must be admin
    events = db.query(event.Event).all()
    return events


# Get all public events
# Filter events by creator / type / start_dt


def get_one(id: int, db: Session):
    found_event = db.query(event.Event).filter(event.Event.id == id).first()
    if not found_event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id: {id} is not available")
    return found_event


def create(request: eventschema.EventIn, db: Session):
    # request.creator = 1  # Set creator from cookie
    new_event = event.Event(title=request.title,
                            desc=request.desc,
                            start_dt=request.start_dt,
                            end_dt=request.end_dt,
                            price=request.price,
                            location=request.location,
                            is_private=request.is_private,
                            creator=request.creator,
                            type=request.type)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


def update(id: int, request: eventschema.EventUpdate, db: Session):
    found_event = db.query(event.Event).filter(event.Event.id == id)

    if not found_event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")

    # Check if user from cookie is the same as creator in found_event or is admin
    found_event.update(request.dict(exclude_unset=True))
    db.commit()
    return found_event.first()


def destroy(id: int, db: Session):
    found_event = db.query(event.Event).filter(event.Event.id == id)

    if not found_event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")

    # Check if user from cookie is the same as creator in found_event or is admin
    found_event.delete(synchronize_session=False)
    db.commit()
    return True
