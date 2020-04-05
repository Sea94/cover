from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from . import db, User


class Request(db.Model):
    table = "request"

    id = Column(Integer, primary_key=True)
    volunteer_id = Column(Integer, ForeignKey('user.id'), default=None)
    name = Column(String(64), nullable=False)
    address = Column(String(100), nullable=False)
    phone = Column(String(64), nullable=False)
    request = Column(String(64), nullable=False)
    category = Column(String(64), nullable=False, default="groceries")  # groceries / pet_walk / social / 
    status = Column(String(10), default="open")  # open / taken / done
    creation_time = Column(DateTime, default=datetime.now)

    # volunteer = relationship("User", foreign_keys=[volunteer_id])

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        return

    @classmethod
    def add(cls, data):
        request = Request(
            name=data["name"],
            phone=data["phone"],
            request=data["request"],
            category=data["category"],
            address=data["address"],
        )
        db.session.add(request)
        db.session.commit()

        return request
