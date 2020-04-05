import json
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from .base import db


class User(UserMixin, db.Model):
    table = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    address = Column(String(100), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    available = Column(Boolean, nullable=False, default=False)
    creation_time = Column(DateTime, default=datetime.now)
    password_hash = Column(String(128), nullable=False)

    # requests = relationship("Request", back_populates="user")


    def dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "available": self.available
        }

    def json(self):
        return json.dumps(self.dict())

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        db.session.commit()

    def get_id(self):
        return self.email

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_available(self, value):
        self.available = value
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def add(cls, data):
        user = User(
            name=data["name"],
            email=data["email"],
            password_hash=generate_password_hash(data["password"]),
        )
        db.session.add(user)
        db.session.commit()

        return user
