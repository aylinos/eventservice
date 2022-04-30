from typing import Optional

from pydantic import BaseModel


# This pydantic model will be used for adding types to the db
class TypeIn(BaseModel):
    title: str


# This pydantic model will be used for getting types from the db
class TypeOut(TypeIn):
    id: int

    class Config:
        orm_mode = True


# This pydantic model will be used for updating the events in the db
# Set the values in the model to be optional => only the field that needs to be updated can be sent
class TypeUpdate(TypeIn):
    title: Optional[str] = None
