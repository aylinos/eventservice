import datetime

from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        String, Text)
from sqlalchemy.orm import relationship

from ..db.session import Base

# from app.db.session import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    desc = Column(Text)
    start_dt = Column(DateTime, nullable=False)
    end_dt = Column(DateTime, nullable=False)
    price = Column(Float, nullable=False)
    location = Column(String, nullable=False)
    is_private = Column(Boolean, default=True)
    creator = Column(Integer, nullable=False)
    type = Column(Integer, ForeignKey("types.id"))
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    date_modified = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    event_type = relationship("Type", back_populates="events")
