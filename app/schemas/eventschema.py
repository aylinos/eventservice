from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# This pydantic model will be used for adding events to the db
class EventIn(BaseModel):
    title: str
    desc: str
    start_dt: datetime
    end_dt: datetime
    price: float
    location: str
    is_private: bool
    creator: int
    type: int


# This pydantic model will be used for getting events from the db
class EventOut(EventIn):
    id: int

    class Config:
        orm_mode = True


# This pydantic model will be used for updating the events in the db
# Set the values in the model to be optional => only the field that needs to be updated can be sent
class EventUpdate(EventIn):
    title: Optional[str] = None
    desc: Optional[str] = None
    start_dt: Optional[datetime] = None
    end_dt: Optional[datetime] = None
    price: Optional[float] = None
    location: Optional[str] = None
    is_private: Optional[bool] = None
    type: Optional[int] = None
