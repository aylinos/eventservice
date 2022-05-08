from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..db.session import Base

# from app.db.session import Base


class Type(Base):
    __tablename__ = "types"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)

    # events = relationship('Event', back_populates="event_type")
    events = relationship(
        "Event",
        cascade="all,delete-orphan",
        back_populates="event_type",
        uselist=True,
    )
