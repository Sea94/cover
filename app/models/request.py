from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from . import db, User


class Request(db.Model):
    table = "request"

    id = Column(Integer, primary_key=True)
    volunteer_id = Column(Integer, ForeignKey('user.id'), default=None)
    name = Column(String(64), nullable=False)
    address = Column(String(100), nullable=False)
    latitude = Column(Float())
    longitude = Column(Float())
    phone = Column(String(64), nullable=False)
    request = Column(String(64), nullable=False)
    category = Column(String(64), nullable=False, default="grocery")  # grocery / pet_walk / social / 
    status = Column(String(10), default="open")  # open / taken / done
    creation_time = Column(DateTime, default=datetime.now)

    volunteer = relationship("User", foreign_keys=[volunteer_id])

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        return

    @classmethod
    def set_volunteer(cls, rid, volunteer):
        req = Request.query.get(rid)
        if req.volunteer is not None:
            return
        req.volunteer = volunteer
        req.status = "taken"
        db.session.commit()

    @classmethod
    def set_done(cls, rid, volunteer):
        req = Request.query.get(rid)
        if req.volunteer != volunteer:
            return
        req.status = "done"
        db.session.commit()

    @classmethod
    def add(cls, data):
        request = Request(
            name=data["name"],
            phone=data["phone"],
            request=data["request"],
            category=data["category"],
            address=data["address"],
            latitude=data["latitude"],
            longitude=data["longitude"],
        )
        db.session.add(request)
        db.session.commit()

        return request
